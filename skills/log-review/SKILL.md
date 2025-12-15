---
name: log-review
description: Inspect error logs quickly; use when log snippets or stack traces are mentioned.
---

# Log Review
- Scan logs for errors and stack traces; summarize root causes and impacted services.
- Suggest next diagnostic commands (e.g., `rg "ERROR"`, `journalctl -xe`, or service-specific logs).
- When possible, propose a minimal reproduction based on failing log entries.
