<div align="center">

# Codex Cheat Sheet

<a href="https://openai.com/codex/"><img width="763" height="341" alt="Codex cheat sheet" src="assets/image.png" /></a>

> A working reference for the OpenAI Codex CLI. Every command below was checked against `codex-cli 0.164.0` and the [official docs](https://developers.openai.com/codex).

</div>

## Quick Start

```bash
# Install (macOS/Linux)
curl -fsSL https://chatgpt.com/codex/install.sh | sh

# Or with npm
npm install -g @openai/codex

# Or with Homebrew
brew install --cask codex

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"

# Launch and check the version
codex
codex --version
```

## Table of Contents

- **[Level 1: Getting Started](#level-1-getting-started)**
- **[Level 2: Basic Commands](#level-2-basic-commands)**
- **[Level 3: Intermediate Usage](#level-3-intermediate-usage)**
- **[Level 4: Advanced Features](#level-4-advanced-features)**
- **[Skills](#skills)** — Native, reusable capabilities
- **[Level 5: Expert Workflows](#level-5-expert-workflows)**

## Level 1: Getting Started

<details>
<summary><strong>Installation</strong></summary>

```bash
# Official standalone installer (macOS/Linux)
curl -fsSL https://chatgpt.com/codex/install.sh | sh

# npm
npm install -g @openai/codex

# Homebrew
brew install --cask codex

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"

# Update
codex update                              # self-update, when the install supports it
npm install -g @openai/codex              # update an npm install
brew upgrade --cask codex                 # update a Homebrew install

# Manual download
# https://github.com/openai/codex/releases/latest
```

`pnpm install -g @openai/codex` also works and the updater recognizes it, but the official install docs list only npm, Homebrew, and the standalone scripts.

</details>

<details>
<summary><strong>First Steps</strong></summary>

```bash
codex                                     # interactive mode
codex "explain this project"              # start with a prompt
codex exec "explain utils.ts"             # non-interactive
```

</details>

<details>
<summary><strong>Authentication</strong></summary>

```bash
codex                                     # then pick "Sign in with ChatGPT"
codex login status                        # exit 0 means credentials are present

printenv OPENAI_API_KEY | codex login --with-api-key
printenv CODEX_ACCESS_TOKEN | codex login --with-access-token
codex login --device-auth                 # device authentication
codex logout                              # remove stored credentials
```

</details>

<details>
<summary><strong>Basic Navigation</strong></summary>

```bash
# Keyboard shortcuts
Ctrl+C                    # cancel the current operation
Tab                       # queue a follow-up prompt or slash command while Codex works
↑/↓                       # restore draft history
Esc Esc                   # edit the previous message (forks the chat from that point)
Ctrl+R                    # search prompt history
Ctrl+O                    # copy the latest completed output
Enter                     # inject new instructions into the running turn
!command                  # run a local shell command under the current approval/sandbox rules

@                         # trigger file search
```

</details>

## Level 2: Basic Commands

<details>
<summary><strong>Slash Commands</strong></summary>

Type `/` in the TUI to see the list for your build. The commands in 0.164.0:

```bash
# Session
/new                      # start a new chat
/resume                   # resume a saved chat
/fork                     # fork the conversation into a new thread
/rename                   # rename the current chat
/archive                  # archive the current session and exit
/delete                   # permanently delete the current session and exit
/compact                  # summarize the conversation to free up context
/undo                     # undo recent turns
/status                   # show session config and token usage
/usage                    # view account token usage
/cd <dir>                 # change the working directory
/pwd                      # print the working directory (alias: /cwd)
/worktree                 # start the session in a Git worktree

# Model and behavior
/model                    # choose model and reasoning effort
/presets                  # choose a power preset
/permissions              # configure what Codex can do without approval
/plan                     # switch to plan mode for multi-step work
/goal                     # set or view a persistent task goal
/approve                  # approve one retry of an automatic-review denial
/experimental             # toggle experimental features
/config                   # inspect the resolved configuration
/debug-config             # print config layer diagnostics
/fast                     # toggle Fast mode (only when your model catalog offers it)

# Code and review
/review                   # review current changes and find issues
/diff                     # show git diff, including untracked files
/mention                  # mention a file
/init                     # create an AGENTS.md with instructions
/recap                    # summarize what happened in the session

# Tools and extensions
/mcp                      # list configured MCP tools
/skills                   # browse and use skills
/plugins                  # browse installed and discoverable plugins
/apps                     # browse apps (connectors)
/hooks                    # view and manage lifecycle hooks
/memories                 # configure memory use and generation
/import                   # import Claude Code or Cursor setup
/ide                      # include open files and IDE context

# Environment and shell
/cd                       # change directory
/pwd                      # print working directory
/ps                       # show background terminals and their output
/stop                     # stop all background terminals (alias: /clean)
/raw                      # toggle raw scrollback mode
/daemon                   # manage the shared app-server daemon
/voice                    # voice input
/daybreak                 # Daybreak access program
/setup-default-sandbox    # pick a default sandbox (Windows)

# Session output and appearance
/copy                     # copy the latest completed output (or Ctrl+O)
/export                   # export the session
/tui                      # TUI preferences
/title                    # terminal title
/statusline               # footer items
/theme                    # choose a syntax theme
/pets                     # choose or hide a terminal pet (alias: /pet)
/keymap                   # remap keyboard shortcuts
/vim                      # toggle Vim mode in the composer

# End of session
/logout                   # log out
/quit                     # exit Codex
/exit                     # exit Codex
/feedback                 # send logs to maintainers
```

Two notes on the older list of commands. `/personality` is not a CLI slash command; it belongs to the IDE extension. The agent switcher is `/agents` (plural), and `/subagents` also works.

</details>

<details>
<summary><strong>File and Directory Operations</strong></summary>

```bash
# Ask Codex to read, write, or edit
"Read the contents of src/app.js"
"Create a new file called utils.js"
"Edit the function in main.py to add error handling"

# Inspect a project
"Explain the structure of this project"
"What files are in the src directory?"
```

</details>

<details>
<summary><strong>Session Management</strong></summary>

```bash
codex resume                          # open the session picker
codex resume --last                   # resume the most recent session
codex resume <SESSION_ID>             # resume a specific session
codex fork <SESSION_ID>               # fork a session into a new chat
codex fork --last                     # fork the most recent session

codex exec resume --last              # resume a non-interactive session
codex exec resume <SESSION_ID>
codex exec fork <SESSION_ID>

codex archive <SESSION>               # archive a saved session
codex unarchive <SESSION>             # restore it
codex delete <SESSION>                # permanently delete it
codex queue --thread <ID> --message "text"   # queue a message for a running session
```

</details>

<details>
<summary><strong>Subcommand Reference</strong></summary>

| Command | Purpose |
|---|---|
| `codex exec` | Run non-interactively (alias: `e`) |
| `codex review` | Non-interactive code review |
| `codex login` / `codex logout` | Manage authentication; `codex login status` checks credentials |
| `codex resume` | Resume a saved session (picker; `--last` for most recent) |
| `codex fork` | Fork a session into a new chat |
| `codex archive` / `codex unarchive` | Archive and restore saved sessions |
| `codex delete` | Permanently delete a session |
| `codex queue` | Queue a message for an existing session (`--thread`, `--message`) |
| `codex agents` | Browse agent sessions on the shared local app-server daemon |
| `codex apply` | Apply a Codex Cloud agent diff to your working tree (alias: `a`) |
| `codex cloud` | Browse or execute Codex Cloud tasks (experimental) |
| `codex plugin` | Install, list, and remove plugins; `codex plugin marketplace` manages sources |
| `codex mcp` | Manage MCP servers (list, get, add, remove, login, logout) |
| `codex app-server` | Run the app server (experimental) |
| `codex remote-control` | Manage the app-server daemon with remote control (experimental) |
| `codex doctor` | Diagnose install, config, auth, and runtime health |
| `codex features` | Inspect feature flags (list, enable, disable) |
| `codex sandbox` | Run a command inside a Codex-provided sandbox |
| `codex update` | Self-update to the latest version |
| `codex completion` | Generate shell completions (bash, elvish, fish, powershell, zsh) |
| `codex exec-server` | Run the standalone exec-server service (experimental) |
| `codex debug` | Debugging tools (`models`, `app-server`, `prompt-input`) |
| `codex migrate-rollouts` | Inspect or migrate legacy local session storage |
| `codex migrate-nfs-db` | Migrate configured SQLite databases to DELETE mode (experimental) |

`codex mcp-server` was removed. Use the app server instead.

`codex app` only exists on macOS and Windows builds.

</details>

<details>
<summary><strong>Useful CLI Flags</strong></summary>

```bash
# Model selection
codex --model gpt-6.1-sol "your prompt"
codex -m gpt-6-astra "hardest task"

# Working directory
codex --cd /path/to/project
codex -C ../other-project
codex --add-dir ../backend --add-dir ../shared "analyze all"
codex --worktree                          # run in a new managed Git worktree

# Approval settings
codex -a on-request                       # the model decides when to ask
codex exec -a never "task"                # never ask

# Sandbox settings
codex --sandbox read-only                 # default
codex --sandbox workspace-write
codex --sandbox danger-full-access        # no sandbox, dangerous

# Feature flags
codex --enable <FEATURE>
codex --disable <FEATURE>

# Image input
codex -i screenshot.png "explain this error"
codex --image img1.png,img2.jpg "summarize these diagrams"

# Live web search
codex --search "what is the latest version of X"

# Approval automation
codex --approve-for-me "refactor this"
codex --dangerously-bypass-approvals-and-sandbox "task"   # also spelled --yolo

# Strict config
codex --strict-config                     # fail on unknown config.toml fields

# Local open-source providers
codex --oss
codex --oss --local-provider ollama       # or lmstudio

# Config profiles
codex -p work "your prompt"               # layers ~/.codex/work.config.toml

# Remote app server
codex --remote ws://host:port
codex --remote wss://host:port --remote-auth-token-env TOKEN_ENV

# Terminal and daemon
codex --no-alt-screen                     # run inline, keep scrollback
codex --no-daemon                         # skip the shared background server

# Shell completions
codex completion zsh
```

</details>

## Level 3: Intermediate Usage

<details>
<summary><strong>Configuration</strong></summary>

```bash
# User config: ~/.codex/config.toml
# Project config: .codex/config.toml (trusted projects only;
#   provider, auth, notification, and telemetry keys are ignored there)

codex --model gpt-6.1-sol "your prompt"
codex --config model="gpt-6.1-sol"
codex --config 'compaction.keep.tokens=20000'

# Useful config.toml keys
# model, model_reasoning_effort, approval_policy, sandbox_mode,
# mcp_servers, profiles, features
```

</details>

<details>
<summary><strong>Model Selection</strong></summary>

```bash
model = "gpt-6.1-sol"               # Recommended for complex, repeated work
model = "gpt-6-astra"              # Most capable; hardest end-to-end work
model = "gpt-6-sol"                # Previous Sol generation
model = "gpt-6-luna"               # Fastest and cheapest; focused, high-volume tasks
model = "gpt-5.6-sol"              # Previous generation, still available during rollout
model = "gpt-5.6-terra"
model = "gpt-5.6-luna"

# Reasoning effort
model_reasoning_effort = "high"    # low, medium, high, xhigh

# Available models as of October 2026
# - gpt-6.1-sol   - near-Astra performance at a lower cost than Astra (recommended)
# - gpt-6-astra  - most capable: code, apps, and research
# - gpt-6-sol    - previous Sol generation
# - gpt-6-luna   - most efficient for focused, high-volume tasks
# - gpt-5.6-sol / gpt-5.6-terra / gpt-5.6-luna - available during the rollout
# - gpt-5.5      - retired from Codex with ChatGPT sign-in on Oct 14, 2026
# - gpt-5.4 / gpt-5.4-mini - retired with ChatGPT sign-in on Aug 31, 2026
# - gpt-5.2 / gpt-5.3-codex - deprecated in Codex with ChatGPT sign-in
# - gpt-5.3-codex-spark - retired from the CLI and IDE on Sep 14, 2026

# Other models through custom providers
codex --oss --local-provider ollama
```

`codex debug models` prints the catalog available to your account, which is the fastest way to see what you can actually pick.

Replacements for retired models:

| Retired | Use instead |
|---|---|
| `gpt-5.5` | `gpt-6.1-sol`, or `gpt-6-luna` on Free and Go plans |
| `gpt-5.4` | `gpt-6-sol` |
| `gpt-5.4-mini` | `gpt-6-luna` |
| `gpt-5.3-codex-spark` | `gpt-6.1-sol` |

Retirements only affect sessions signed in with ChatGPT. API-key sessions are unaffected. See the [official Models page](https://developers.openai.com/codex/models).

</details>

<details>
<summary><strong>Reasoning Effort</strong></summary>

```bash
model_reasoning_effort = "low"       # Light in the desktop app
model_reasoning_effort = "medium"
model_reasoning_effort = "high"
model_reasoning_effort = "xhigh"     # Extra High in the desktop app
```

Max and Ultra exist on some models and plans. Ultra runs subagents, so it can split a large task into parallel pieces. GPT-6 Luna supports up to Max but not Ultra.

</details>

<details>
<summary><strong>Custom Prompts</strong></summary>

```bash
# Create ~/.codex/prompts/review.md, then invoke it
"Use the review prompt on this code"
```

</details>

<details>
<summary><strong>Memory with AGENTS.md</strong></summary>

```markdown
# AGENTS.md in the project root

This project uses:
- Node.js with Express
- PostgreSQL
- Jest for testing

Coding standards:
- Use TypeScript
- Follow ESLint rules
- Write tests for new features
```

Codex reads `AGENTS.md` from the project root on every run.

</details>

## Level 4: Advanced Features

<details>
<summary><strong>Model Context Protocol (MCP)</strong></summary>

```bash
# STDIO server
[mcp_servers.filesystem]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
env = { API_KEY = "value" }

# Streamable HTTP server
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_TOKEN"

# MCP CLI commands
codex mcp list                        # list configured servers
codex mcp add <name> -- <command>     # add a stdio server
codex mcp add <name> --url <URL>      # add a streamable HTTP server
codex mcp get <name>                  # show server details
codex mcp remove <name>               # remove a server
codex mcp login <name>                # OAuth login
codex mcp logout <name>               # OAuth logout

# Fail startup if a server cannot initialize
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
required = true

# Plugins are the stable surface for packaged integrations
codex plugin list
codex plugin add <plugin>             # or PLUGIN@MARKETPLACE
codex plugin marketplace list
```

See [MCP Documentation](https://developers.openai.com/codex/configuration) for details.

</details>

<details>
<summary><strong>Sandbox and Permissions</strong></summary>

```bash
# Sandbox mode
sandbox_mode = "read-only"              # default
sandbox_mode = "workspace-write"
sandbox_mode = "danger-full-access"     # no sandbox, dangerous

# Approval policy
approval_policy = "on-request"          # the model decides when to ask
approval_policy = "never"               # never ask

# Granular approval, if you want it per category
approval_policy = { granular = { sandbox_approval = true, mcp_elicitations = true } }

# Workspace-write options
[sandbox_workspace_write]
writable_roots = ["/path/to/extra/dir"]
network_access = false
exclude_tmpdir_env_var = false
exclude_slash_tmp = false
```

`approval_policy = "untrusted"` is no longer supported. The CLI flag accepts only `on-request` and `never`. The old `on-failure` value is a deprecated alias of `on-request`.

See [Sandbox and Approvals](https://developers.openai.com/codex/sandboxing) for details.

</details>

<details>
<summary><strong>Non-Interactive Mode</strong></summary>

```bash
codex exec "summarize all TODO comments in this project"

# Auto-review approvals (workspace-write sandbox, automatic review)
codex exec --approve-for-me "refactor this code"

# Fully unattended (no approvals, no sandboxing)
codex exec --dangerously-bypass-approvals-and-sandbox "refactor this code"

# JSON output for automation
codex exec --json "analyze this project"

# Structured output with a JSON schema
codex exec --output-schema schema.json "extract project details"

# Write the last message to a file
codex exec -o output.txt "generate docs"

# JSONL events to stdout, summary to the file
codex exec --json -o output.txt "generate docs"

# Useful in CI
codex exec --skip-git-repo-check --ignore-user-config "summarize this repo"
codex exec --ephemeral "one-off analysis"    # do not persist the session
```

`codex exec` also has `resume`, `fork`, and `review` subcommands.

See [Non-Interactive Mode (exec)](https://developers.openai.com/codex/non-interactive-mode) for details.

</details>

<details>
<summary><strong>Non-Interactive Code Review</strong></summary>

Runs a review without launching the TUI. Reports prioritized findings and leaves the working tree alone.

```bash
codex review --uncommitted                    # staged, unstaged, and untracked
codex review --base main                      # compare against a base branch
codex review --commit <SHA>                   # review one commit
codex review --uncommitted --title "wip: auth"
codex review "focus on security issues"       # custom instructions
```

See [Code Review](https://developers.openai.com/codex/code-review) for details.

</details>

<details>
<summary><strong>Piping and Scripting</strong></summary>

```bash
cat logs.txt | codex exec "find the error"
git diff | codex exec "create a conventional commit message"
codex exec "explain this file" < app.js > explanation.md
```

</details>

<details>
<summary><strong>Skills</strong></summary>

<a id="skills"></a>

- **What they are:** On-disk capabilities Codex discovers automatically. Each skill is a folder with a `SKILL.md` that has `name`, `description`, and an optional body.
- **Where skills live:** `~/.codex/skills/**/SKILL.md`. Only files named exactly `SKILL.md` count; hidden entries and symlinks are skipped.
- **File format:**
  ```markdown
  ---
  name: your-skill-name          # required, 100 chars max, one line
  description: when/why to use   # required, 500 chars max, one line
  ---

  Add references, workflows, or examples here.
  ```
- **Using skills:** Mention one with `$<skill-name>` in chat, or browse and insert via `/skills`. Codex injects the name, description, and file path, then loads the body on demand.
- **Validation:** Bad frontmatter raises a dismissible startup modal and log entries. Invalid skills are ignored until you fix them.
- **Sample skills in this repo.** Copy one into `~/.codex/skills/<name>/SKILL.md` and restart Codex:
  - `skills/pdf-processing/SKILL.md`
  - `skills/log-review/SKILL.md`
  - `skills/form-filling/SKILL.md`
  - `skills/project-management/SKILL.md`
- **Community alternative:** [openskills](https://github.com/numman-ali/openskills) is still a reasonable choice if you prefer a community-driven skills system.

</details>

<details>
<summary><strong>Task Goals</strong></summary>

`/goal` sets a persisted objective for a long-running task. It loops plan, act, test, and review until your stop condition is met.

```bash
/goal Finish the migration and keep tests green    # set a goal
/goal                                               # view the current goal
/goal pause                                         # pause the run
/goal resume                                        # resume a paused run
/goal clear                                         # clear the goal
```

Use it for multi-hour work with a clear definition of done. Skip it while you are still exploring.

Give the goal one measurable stop condition. Use `/goal pause` or `/goal clear` if it drifts, and run it on a scratch branch.

See [OpenAI's goal docs](https://developers.openai.com/codex/developer-commands) for details.

</details>

## Level 5: Expert Workflows

<details>
<summary><strong>GitHub Actions Integration</strong></summary>

```yaml
name: Code Review
on: [pull_request]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: openai/codex-action@v1
        with:
          task: "Review this PR for security issues"
```

See [GitHub Action](https://github.com/openai/codex-action) for details.

</details>

<details>
<summary><strong>Automated Code Review</strong></summary>

```bash
codex "Review this PR for security, performance, and maintainability"
git diff HEAD~1 | codex exec "Create a conventional commit message"
codex "Fix all ESLint errors in this project"
```

</details>

<details>
<summary><strong>CI/CD Pipeline Assistance</strong></summary>

```bash
codex "Create a GitHub Actions workflow that runs tests on PR and deploys to Vercel on main"
cat .github/workflows/build.log | codex exec "Find the root cause"
```

</details>

<details>
<summary><strong>Legacy Code Migration</strong></summary>

```bash
codex "Convert this Python utility to TypeScript"
codex "Update all React class components to functional components with hooks"
codex "Add TypeScript types to this JavaScript project"
```

</details>

<details>
<summary><strong>Performance Optimization</strong></summary>

```bash
codex "Profile this code and identify performance bottlenecks"
codex "Refactor these N+1 queries to use batch loading"
codex "Suggest webpack optimizations to reduce bundle size"
```

</details>

<details>
<summary><strong>Security Auditing</strong></summary>

```bash
codex "Audit this code for security vulnerabilities"
codex "Review package.json for outdated or vulnerable dependencies"
codex "Check if this code follows OWASP security guidelines"
```

</details>

<details>
<summary><strong>Troubleshooting and Debugging</strong></summary>

```bash
cat error.log | codex exec "find the root cause"
codex "Debug why the login function is failing"
codex "Create a test case that reproduces this bug, then fix it"

codex doctor               # install, config, auth, and runtime health
codex doctor --json        # machine-readable output
```

</details>

<details>
<summary><strong>Documentation</strong></summary>

```bash
codex exec "Create a README for this project"
codex exec "Generate API docs from JSDoc comments"
codex "Add explanatory comments to this complex function"
```

</details>

<details>
<summary><strong>Testing</strong></summary>

```bash
codex "Create unit tests for all functions in utils.js"
codex "Analyze test coverage and suggest missing tests"
codex "Create Playwright E2E tests for the user flow"
```

</details>

<details>
<summary><strong>Refactoring</strong></summary>

```bash
codex "Refactor this code to:
1. Improve readability
2. Add error handling
3. Follow TypeScript best practices
4. Add type definitions"
```

</details>

## Additional Resources

**Official documentation:**
- [Codex docs](https://developers.openai.com/codex) - Documentation hub
- [Quickstart](https://developers.openai.com/codex/quickstart) - Getting started
- [Configuration](https://developers.openai.com/codex/configuration) - Full `config.toml` reference
- [Developer commands](https://developers.openai.com/codex/developer-commands) - CLI commands and slash commands
- [Non-interactive mode](https://developers.openai.com/codex/non-interactive-mode) - Automation with `codex exec`
- [Authentication](https://developers.openai.com/codex/auth) - Sign-in methods
- [Sandbox and approvals](https://developers.openai.com/codex/sandboxing) - Security model
- [AGENTS.md](https://developers.openai.com/codex/agent-configuration/agents-md) - Project instructions
- [Models](https://developers.openai.com/codex/models) - Model list and retirements
- [Skills and plugins](https://developers.openai.com/codex/skills-and-plugins) - Official guide
- [Troubleshooting](https://developers.openai.com/codex/reference/troubleshooting) - FAQ

**Extensions and integrations:**
- [GitHub Action](https://github.com/openai/codex-action) - CI/CD integration
- [TypeScript SDK](https://developers.openai.com/codex/codex-sdk) - Programmatic use
- [IDE extension](https://developers.openai.com/codex/ide) - VS Code and friends

**Related tools:**
- [Kimi Cheat Sheet](https://github.com/BA-CalderonMorales/kimi-cheat-sheet) - Companion guide for Kimi Code CLI
- [OpenCode Cheat Sheet](https://github.com/BA-CalderonMorales/opencode-cheat-sheet) - Companion guide for OpenCode

**Model Context Protocol:**
- [MCP specification](https://modelcontextprotocol.io/) - Protocol docs
- [MCP server examples](https://github.com/modelcontextprotocol/servers) - Community servers

## Contributing

Corrections are welcome. Report anything that no longer matches `codex --help`.

- Report bugs or inconsistencies
- Suggest new examples
- Improve documentation
- Share your workflows

## License

MIT License. Free to use and modify.

## Credits

This structure grew out of [claude-code-cheat-sheet](https://github.com/Njengah/claude-code-cheat-sheet) by @Njengah.

---

**Last updated: October 2026**
**Based on**: OpenAI Codex CLI (codex-cli 0.164.0, npm: `@openai/codex`)
