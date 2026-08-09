#!/usr/bin/env python3
"""Conservative README checker:
- Finds HTTP(S) links in README.md
- Attempts a quick HEAD (then GET) to validate links (timeouts kept short)
- Applies only safe, obvious fixes (http://github.com -> https://github.com, http://img.shields.io -> https://img.shields.io)
- Writes back README.md when edits were made so the workflow can commit them
- Exits 0 on success (even if broken links were detected). Non-zero only on unexpected errors.
"""

from __future__ import annotations
import re
import sys
import ssl
import urllib.request
import urllib.error
from urllib.parse import urlparse
from typing import List, Tuple

README = "README.md"
TIMEOUT = 10

link_re = re.compile(r"\[.*?\]\((https?://[^\s)]+)\)")
autolink_re = re.compile(r"<https?://[^>]+>")
bare_re = re.compile(r"(?<!\()(?<!\[)(https?://[^\s)\]>]+)")


def find_links(text: str) -> List[str]:
    seen = []
    for m in link_re.findall(text):
        if m not in seen:
            seen.append(m)
    for m in re.findall(r"<(https?://[^>]+)>", text):
        if m not in seen:
            seen.append(m)
    for m in bare_re.findall(text):
        if m not in seen:
            seen.append(m)
    return seen


def safe_fix(url: str) -> Tuple[str, bool]:
    """Return (possibly_fixed_url, changed_bool). Only apply extremely safe changes."""
    if url.startswith("http://github.com"):
        return ("https://" + url[len("http://"):], True)
    if url.startswith("http://img.shields.io"):
        return ("https://" + url[len("http://"):], True)
    return (url, False)


def is_broken(url: str) -> Tuple[bool, str]:
    """Return (is_broken, reason). Network problems are treated as 'possibly broken' but not fatal."""
    ctx = ssl.create_default_context()
    headers = {"User-Agent": "readme-check/1.0 (+https://github.com)"}
    # Try HEAD first
    try:
        req = urllib.request.Request(url, headers=headers, method="HEAD")
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
            code = resp.getcode()
            if code >= 400:
                return True, f"HTTP {code}"
            return False, "OK"
    except TypeError:
        # Older runtimes may not accept method on Request; fall back to GET
        pass
    except urllib.error.HTTPError as e:
        return True, f"HTTP {e.code}"
    except Exception as e:  # network errors, timeouts
        # Try GET as fallback to handle servers that don't respond to HEAD
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
                code = resp.getcode()
                if code >= 400:
                    return True, f"HTTP {code}"
                return False, "OK"
        except Exception as e2:
            return True, f"NetworkError: {e2}"
    # If we get here, the HEAD succeeded above
    return False, "OK"


def main() -> int:
    try:
        with open(README, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"{README} not found; nothing to do.")
        return 0

    links = find_links(text)
    if not links:
        print("No links found in README.")
        return 0

    changed = False
    broken = []
    edits = []
    new_text = text

    for url in links:
        fixed_url, did_fix = safe_fix(url)
        if did_fix:
            # Replace only exact occurrences to avoid accidental rewrites
            new_text = new_text.replace(url, fixed_url)
            edits.append((url, fixed_url))
            changed = True
            print(f"Applied safe fix: {url} -> {fixed_url}")
            url_to_check = fixed_url
        else:
            url_to_check = url

        is_bad, reason = is_broken(url_to_check)
        if is_bad:
            broken.append((url_to_check, reason))
            # Do not attempt risky repairs; just report
            print(f"Possible broken link: {url_to_check} ({reason})")

    if changed:
        try:
            with open(README, "w", encoding="utf-8") as f:
                f.write(new_text)
            print(f"Wrote {README} with {len(edits)} safe edits.")
        except Exception as e:
            print(f"Failed to write {README}: {e}", file=sys.stderr)
            return 2

    # Summary
    if broken:
        print("Summary: Found possible broken links:")
        for u, r in broken:
            print(f" - {u}: {r}")
    else:
        print("Summary: No broken links detected (quick check).")

    # Exit 0 on success. Non-zero only for unexpected failures above.
    return 0


if __name__ == "__main__":
    sys.exit(main())