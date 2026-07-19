<div align="center">

# Codex Cheat Sheet

<a href="https://openai.com/codex/"><img width="763" height="341" alt="Codex cheat sheet" src="assets/image.png" /></a>

> **Your complete guide to mastering OpenAI Codex — from zero to productive in minutes.**

A practical reference for using OpenAI Codex CLI effectively. Focuses on patterns that help you think critically about what to delegate and what to handle yourself.

**Based on official OpenAI Codex documentation** - All commands and examples are sourced from the [official Codex documentation](https://developers.openai.com/codex). For the most up-to-date information, always refer to the official docs.

</div>

## Quick Start

```bash
# Install with the official installer (recommended)
curl -fsSL https://chatgpt.com/codex/install.sh | sh

# Or with npm
npm install -g @openai/codex

# Or with Homebrew
brew install --cask codex

# Or with pnpm (official monorepo manager)
pnpm install -g @openai/codex

# Windows: Direct install script
# Run: .\install.ps1 from https://github.com/openai/codex/releases

# Launch Codex
codex

# Check version
codex --version
```

## Table of Contents

- **[Level 1: Getting Started](#level-1-getting-started)**
- **[Level 2: Basic Commands](#level-2-basic-commands)**
- **[Level 3: Intermediate Usage](#level-3-intermediate-usage)**
- **[Level 4: Advanced Features](#level-4-advanced-features)**
- **[Skills (experimental)](#skills-experimental)** - Native, reusable capabilities with feature flag
- **[Level 5: Expert Workflows](#level-5-expert-workflows)**
- **[Command Reference](#command-reference)**
- **[Best Practices](#best-practices)**

## Level 1: Getting Started

Essential commands to get you started with Codex.

<details>
<summary><strong>Installation</strong></summary>

```bash
# Install globally with npm
npm install -g @openai/codex

# Install with Homebrew (macOS)
brew install --cask codex

# Install with pnpm (official monorepo manager)
pnpm install -g @openai/codex

# Update with npm
npm update -g @openai/codex

# Update with Homebrew
brew upgrade codex

# Windows: Use the install.ps1 script
# Download from: https://github.com/openai/codex/releases/latest
# Run: .\install.ps1

# Download binary from GitHub releases
# Visit: https://github.com/openai/codex/releases/latest
```

</details>

<details>
<summary><strong>First Steps</strong></summary>

```bash
# Start interactive mode
codex

# Run with a specific prompt
codex "explain this project"

# Non-interactive execution
codex exec "explain utils.ts"
```

</details>

<details>
<summary><strong>Authentication</strong></summary>

```bash
# Sign in with ChatGPT account (recommended)
codex
# Then select "Sign in with ChatGPT"

# Use API key (alternative - usage-based billing)
printenv OPENAI_API_KEY | codex login --with-api-key
# Or from a file:
codex login --with-api-key < my_key.txt
```

</details>

<details>
<summary><strong>Basic Navigation</strong></summary>

```bash
# Keyboard shortcuts
Ctrl+C                    # Cancel current operation
Ctrl+D                    # Exit Codex
Tab                       # Auto-complete
↑/↓                       # Command history
Esc Esc                   # Edit previous message

# Special input
@                         # Trigger file search (fuzzy find)
```

</details>

## Level 2: Basic Commands

Core commands for everyday use.

<details>
<summary><strong>Slash Commands - Essentials</strong></summary>

```bash
/model                    # Choose model and reasoning effort
/approvals                # Configure what Codex can do without approval
/review                   # Review current changes and find issues
/new                      # Start a new chat during conversation
/init                     # Create an AGENTS.md file with instructions
/compact                  # Summarize conversation to prevent context limit
/debug                    # Toggle debug mode for detailed logging
/diff                     # Show git diff (including untracked files)
/mention                  # Mention a file
/status                   # Show current session config and token usage
/mcp                      # List configured MCP tools
/logout                   # Log out of Codex
/quit                     # Exit Codex
/exit                     # Exit Codex
/feedback                 # Send logs to maintainers
/goal                     # Set or view a persistent task goal
```

</details>

<details>
<summary><strong>File and Directory Operations</strong></summary>

```bash
# Codex can read, write, and edit files
"Read the contents of src/app.js"
"Create a new file called utils.js"
"Edit the function in main.py to add error handling"

# View project structure
"Explain the structure of this project"
"What files are in the src directory?"
```

</details>

<details>
<summary><strong>Working with Code</strong></summary>

```bash
# Code analysis
"Explain what this code does"
"Review this function for bugs"
"Suggest improvements for this file"

# Code generation
"Write a function to parse JSON"
"Create unit tests for this module"
"Add error handling to this code"
```

</details>

<details>
<summary><strong>Session Management</strong></summary>

```bash
# Resume sessions
codex resume                          # Open session picker
codex resume --last                   # Resume most recent session
codex resume <SESSION_ID>             # Resume specific session by ID

# Non-interactive session resume
codex exec resume <SESSION_ID>        # Resume non-interactive session
codex exec resume --last              # Resume last non-interactive session
```

</details>

<details>
<summary><strong>Useful CLI Flags</strong></summary>

```bash
# Model selection
codex --model gpt-5 "your prompt"
codex -m o3 "complex task"

# Working directory
codex --cd /path/to/project           # Change working directory
codex -C ../other-project             # Short form

# Multiple directories
codex --add-dir ../backend --add-dir ../shared "analyze all"

# Approval settings
codex --ask-for-approval untrusted    # Ask for untrusted commands
codex -a on-failure                   # Ask on command failure

# Sandbox settings
codex --sandbox read-only             # Read-only sandbox (default)
codex --sandbox workspace-write       # Allow workspace writes
codex --sandbox danger-full-access    # Disable sandbox (dangerous!)

# Image input
codex -i screenshot.png "explain this error"
codex --image img1.png,img2.jpg "summarize these diagrams"

# Shell completions
codex completion bash                 # Generate bash completions
codex completion zsh                  # Generate zsh completions
codex completion fish                 # Generate fish completions
```

</details>

## Level 3: Intermediate Usage

Configuration and customization options.

<details>
<summary><strong>Configuration</strong></summary>

```bash
# Config file location: ~/.codex/config.toml

# Edit config manually or use CLI flags
codex --model gpt-5 "your prompt"
codex --config model="gpt-5"

# Common configurations in config.toml:
# - model selection
# - approval_policy
# - sandbox_mode
# - mcp_servers
# - profiles
```

</details>

<details>
<summary><strong>Model Selection</strong></summary>

```bash
# Set model in config.toml
model = "gpt-5.6-sol"              # Flagship: complex coding, computer use, research (recommended, July 2026)
model = "gpt-5.6-terra"            # Balanced: everyday coding and knowledge work
model = "gpt-5.6-luna"             # Fast: lightweight tasks, lowest cost

# For reasoning models (gpt-5.6-sol, gpt-5.6-terra):
model_reasoning_effort = "medium"  # minimal, low, medium, high
model_reasoning_summary = "auto"   # auto, concise, detailed, none

# For GPT-5 family models:
model_verbosity = "medium"         # low, medium, high

# Models available (as of July 2026):
# - gpt-5.6-sol (recommended) - Flagship for complex coding, computer use, research, security work
# - gpt-5.6-terra - Balances capability and cost for everyday coding and knowledge work
# - gpt-5.6-luna - Fastest, lowest-cost option for lightweight tasks
# - gpt-5 (legacy) - Original GPT-5 (still available)
# - Other OpenAI models via custom providers
```

### GPT-5.6 Updates (July 2026)

**GPT-5.6 Sol** is the new flagship model:
- Purpose-built for complex coding, computer use, research, and security work
- Default Power setting uses Sol with medium reasoning effort
- Superior instruction following and technical accuracy

**GPT-5.6 Terra** balances capability and cost:
- Optimized for everyday coding and knowledge work
- Strong reasoning with efficient token usage

**GPT-5.6 Luna** is the fastest, lowest-cost option:
- Ideal for lightweight tasks and quick iterations
- Maintains quality while minimizing latency

See [GPT-5.6 announcement](https://openai.com/index/gpt-5-6/) for details.

</details>

<details>
<summary><strong>Custom Prompts</strong></summary>

```bash
# Create custom prompts in ~/.codex/prompts/

# Example: Create ~/.codex/prompts/review.md
# Then use with:
"Use the review prompt on this code"
```

</details>

<details>
<summary><strong>Memory with AGENTS.md</strong></summary>

```bash
# Create AGENTS.md in project root
# Codex will remember project-specific context

# Example AGENTS.md content:
"""
This project uses:
- Node.js with Express
- PostgreSQL database
- Jest for testing

Coding standards:
- Use TypeScript
- Follow ESLint rules
- Write tests for all new features
"""
```

</details>

## Level 4: Advanced Features

Powerful features for advanced workflows.

<details>
<summary><strong>Model Context Protocol (MCP)</strong></summary>

```bash
# Configure MCP servers in ~/.codex/config.toml

# STDIO server example
[mcp_servers.filesystem]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
env = { API_KEY = "value" }

# Streamable HTTP server example
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_TOKEN"

# MCP CLI commands
codex mcp list                        # List configured servers
codex mcp add <name> -- <command>     # Add a server
codex mcp get <name>                  # Show server details
codex mcp remove <name>               # Remove a server
codex mcp login <name>                # OAuth login (streamable HTTP)
codex mcp logout <name>               # OAuth logout

# Popular MCP servers:
# - Context7 (developer documentation)
# - Figma (design access)
# - Playwright (browser control)
# - GitHub (GitHub API access)
# - Sentry (log access)
```

See [MCP Documentation](https://developers.openai.com/codex/configuration) for details.

</details>

<details>
<summary><strong>Sandbox & Permissions</strong></summary>

```bash
# Configure sandbox mode in config.toml
sandbox_mode = "read-only"              # Default: read-only
sandbox_mode = "workspace-write"        # Allow writes in workspace
sandbox_mode = "danger-full-access"     # Disable sandbox (dangerous!)

# Configure approval policy
approval_policy = "untrusted"           # Prompt for untrusted commands
approval_policy = "on-failure"          # Prompt on command failure
approval_policy = "on-request"          # Model decides when to ask
approval_policy = "never"               # Never prompt (exec default)

# Workspace-write options
[sandbox_workspace_write]
writable_roots = ["/path/to/extra/dir"]
network_access = false
exclude_tmpdir_env_var = false
exclude_slash_tmp = false
```

See [Sandbox & Approvals](https://developers.openai.com/codex/sandboxing) for details.

</details>

<details>
<summary><strong>Non-Interactive Mode</strong></summary>

```bash
# Execute and exit with codex exec
codex exec "summarize all TODO comments in this project"

# Allow file edits
codex exec --full-auto "refactor this code"

# Full access (dangerous!)
codex exec --sandbox danger-full-access "your task"

# JSON output for automation
codex exec --json "analyze this project"

# Structured output with JSON schema
codex exec --output-schema schema.json "extract project details"

# Save output to file
codex exec -o output.txt "generate docs"
```

See [Non-Interactive Mode (exec)](https://developers.openai.com/codex/non-interactive-mode) for details.

</details>

<details>
<summary><strong>Piping and Scripting</strong></summary>

```bash
# Pipe content to Codex
cat logs.txt | codex exec "find the error"

# Use in scripts
git diff | codex exec "create a comApache-2.0 message"

# Combine commands
codex exec "explain this file" < app.js > explanation.md
```

</details>

<details>
<summary><strong>Skills (experimental)</strong></summary>

<a id="skills-experimental"></a>

> **Warning:** Skills are experimental and may change or be removed at any time before GA. Expect breaking changes and always check the [official skills docs](https://developers.openai.com/codex/skills-and-plugins) for the latest status.

- **What they are:** Native, on-disk reusable capabilities that Codex can auto-discover. Each skill is a bundle with `name`, `description`, and an optional body kept on disk.
- **Enable the feature flag:**  
  - Preferred: add to `~/.codex/config.toml`
    ```toml
    [features]
    skills = true
    ```
  - One-off run: `codex --enable skills`
- **Where skills live:** `~/.codex/skills/**/SKILL.md` (recursive). Only files named exactly `SKILL.md` count; hidden entries and symlinks are skipped.
- **File format (YAML frontmatter + body):**
  ```markdown
  ---
  name: your-skill-name          # required, ≤ 100 chars, single line
  description: when/why to use   # required, ≤ 500 chars, single line
  ---

  # Optional body (kept on disk)
  Add references, workflows, or examples here.
  ```
- **Using skills:** Mention with `$<skill-name>` in chat or browse/insert via `/skills` in the TUI. Codex injects only `name`, `description`, and the absolute file path.
- **Validation behavior:** Invalid frontmatter triggers a dismissible startup modal and log entries; invalid skills are ignored until fixed.
- **Sample skills in this repo:** Copy or symlink any of the samples below into `~/.codex/skills/<name>/SKILL.md`, then restart Codex with the feature flag enabled:
  - `skills/pdf-processing/SKILL.md`
  - `skills/log-review/SKILL.md`
  - `skills/form-filling/SKILL.md`
  - `skills/project-management/SKILL.md`
- **Pair with GitHub Skills:** You can combine Codex skills with the learning paths at [github.com/skills](https://github.com/skills) to onboard teams quickly while keeping reusable Codex guidance locally.
- **Community alternative (pre-native skills):** The [openskills](https://github.com/numman-ali/openskills) project remains a viable open source option if you prefer a community-driven skills system.

</details>

## New Features 2025-2026

Recent additions to Codex that you should know about:

<details>
<summary><strong>Task Goals</strong></summary>

The `/goal` command sets a persisted objective for a long-running task. It loops plan → act → test → review until your stop condition is met.

**Usage:**

```bash
/goal Finish the migration and keep tests green    # Set a goal
/goal                                               # View current goal
/goal pause                                         # Pause the current run
/goal resume                                        # Resume a paused run
/goal clear                                         # Clear the current goal
```

**When to use:** Multi-hour validated work with a clear "done" definition.
**Skip it:** If you are still exploring or making judgment calls.

> **Note:** Define one measurable stop condition. Use `/goal pause` or `/goal clear` if it drifts. Run on a scratch branch.

See [OpenAI's follow-a-goal docs](https://developers.openai.com/codex/cli/slash-commands) for details.

</details>

<details>
<summary><strong>babysit-pr Skill</strong></summary>

The `babysit-pr` skill automates PR maintenance:
- Auto-fixes CI failures
- Handles review comments
- Watches for merge conflicts
- Keeps your PRs moving through the pipeline

```bash
# Use with MCP GitHub integration
codex "babysit this PR with $github"
```

</details>

<details>
<summary><strong>JavaScript REPL (js_repl)</strong></summary>

Persistent JavaScript REPL for incremental code execution:
- Test code snippets in real-time
- Iterate on logic without full re-runs
- Debug complex expressions

```bash
# Enable in config.toml
[mcp_servers.js_repl]
command = "node"
args = ["-e", "process.stdin.on('data', d => eval(d.toString()))"]
```

</details>

<details>
<summary><strong>In-Process App Server</strong></summary>

New architecture for non-interactive `exec` mode:
- Faster startup times
- Better for CI/CD integration
- Reduced overhead for automation scripts

</details>

## AI-Powered Project Management with Codex

Codex isn't just for code - it's a powerful project management assistant. Here's how to leverage it for managing projects, sprints, and tasks:

<details>
<summary><strong>Project Planning & Breakdown</strong></summary>

```bash
# Break down a large feature request
codex "Break down this feature request into actionable tasks:
- User authentication system
- Must support OAuth and email
- Include password reset flow
- Add 2FA option"

# Generate sprint backlog
codex exec "Analyze this project and create a sprint backlog:
- Prioritize by complexity
- Estimate effort in hours
- Identify dependencies"

# Create user stories
codex "Convert these requirements into user stories with acceptance criteria"
```

</details>

<details>
<summary><strong>GitHub Integration for Project Management</strong></summary>

```bash
# Auto-generate PR descriptions
git diff | codex exec "Create a detailed PR description with:
- Summary of changes
- Testing performed
- Breaking changes (if any)"

# Create issues from TODO comments
codex exec "Scan for TODO/FIXME comments and create GitHub issues"

# Generate release notes
codex exec "Create release notes from recent comApache-2.0s"
```

</details>

<details>
<summary><strong>Task Tracking & Status Updates</strong></summary>

```bash
# Generate status report
codex "Review recent comApache-2.0s and generate a status report for stakeholders"

# Track progress
codex "What percentage of sprint tasks are complete based on merged PRs?"

# Risk identification
codex "Analyze this project and identify potential blockers or risks"
```

</details>

<details>
<summary><strong>Team Collaboration Patterns</strong></summary>

```bash
# Code review automation
codex "Review this PR for:
- Security vulnerabilities
- Performance issues
- Code quality standards
- Test coverage gaps"

# Documentation sync
codex "Update the README based on recent feature additions"

# Onboarding assistance
codex "Create a new developer onboarding guide for this project"
```

</details>

<details>
<summary><strong>Creating Project Management Skills</strong></summary>

You can create custom skills for your team's workflow:

```markdown
# ~/.codex/skills/team-sprint/SKILL.md
---
name: team-sprint
description: Manage sprint planning and tracking for our team
---

# Sprint Workflow
1. Use `/standup` to generate daily standup summaries
2. Use `/retro` to collect retrospective feedback
3. Use `/velocity` to calculate team velocity

# Templates
- Sprint planning template in docs/sprint-template.md
- Retrospective format: Start/Stop/Continue
```

</details>

## Level 5: Expert Workflows

Advanced patterns and automation.

<details>
<summary><strong>GitHub Actions Integration</strong></summary>

```yaml
# Use codex-action for CI/CD
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
# Review entire PR
codex "Review this PR for security, performance, and maintainability"

# Generate comApache-2.0 messages
git diff HEAD~1 | codex exec "Create a conventional comApache-2.0 message"

# Auto-fix common issues
codex "Fix all ESLint errors in this project"
```

</details>

<details>
<summary><strong>CI/CD Pipeline Assistance</strong></summary>

```bash
# Generate CI config
codex "Create a GitHub Actions workflow for:
- TypeScript project
- Run tests on PR
- Deploy to Vercel on main"

# Debug CI failures
cat .github/workflows/build.log | codex exec "Find the root cause"
```

</details>

<details>
<summary><strong>Legacy Code Migration</strong></summary>

```bash
# Convert between languages
codex "Convert this Python utility to TypeScript"

# Update deprecated APIs
codex "Update all React class components to functional components with hooks"

# Add type safety
codex "Add TypeScript types to this JavaScript project"
```

</details>

<details>
<summary><strong>Performance Optimization</strong></summary>

```bash
# Analyze bottlenecks
codex "Profile this code and identify performance bottlenecks"

# Optimize database queries
codex "Refactor these N+1 queries to use batch loading"

# Bundle optimization
codex "Suggest webpack optimizations to reduce bundle size"
```

</details>

<details>
<summary><strong>Security Auditing</strong></summary>

```bash
# Find vulnerabilities
codex "Audit this code for security vulnerabilities"

# Dependency checks
codex "Review package.json for outdated or vulnerable dependencies"

# Compliance check
codex "Check if this code follows OWASP security guidelines"
```

</details>

<details>
<summary><strong>Troubleshooting & Debugging</strong></summary>

```bash
# Analyze error logs
cat error.log | codex exec "find the root cause"

# Debug specific function
codex "Debug why the login function is failing"

# Reproduce and fix
codex "Create a test case that reproduces this bug, then fix it"
```

</details>

<details>
<summary><strong>Documentation</strong></summary>

```bash
# Generate README
codex exec "Create a comprehensive README for this project"

# API documentation
codex exec "Generate API docs from JSDoc comments"

# Code comments
codex "Add detailed comments to this complex function"
```

</details>

<details>
<summary><strong>Testing</strong></summary>

```bash
# Generate tests
codex "Create unit tests for all functions in utils.js"

# Test coverage
codex "Analyze test coverage and suggest missing tests"

# E2E test generation
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

**Official OpenAI Codex Documentation:**
- [Official Repository](https://github.com/openai/codex) - Main repository and documentation hub
- [Getting Started Guide](https://developers.openai.com/codex/quickstart) - Comprehensive getting started guide
- [Configuration Reference](https://developers.openai.com/codex/configuration) - Complete config.toml reference
- [Slash Commands](https://developers.openai.com/codex/reference/slash-commands) - All slash commands explained
- [Non-Interactive Mode (exec)](https://developers.openai.com/codex/non-interactive-mode) - Automation with codex exec
- [Authentication](https://developers.openai.com/codex/auth) - Authentication methods
- [Sandbox & Approvals](https://developers.openai.com/codex/sandboxing) - Security and sandboxing
- [AGENTS.md Documentation](https://developers.openai.com/codex/agent-configuration/agents-md) - Project instructions guide
- [MCP Integration](https://developers.openai.com/codex/configuration) - MCP setup and usage
- [Custom Prompts](https://developers.openai.com/codex/prompting) - Creating custom prompts
- [FAQ](https://developers.openai.com/codex/reference/troubleshooting) - Frequently asked questions
- [Skills (experimental)](https://developers.openai.com/codex/skills-and-plugins) - Official guide

**Extensions & Integrations:**
- [GitHub Action](https://github.com/openai/codex-action) - CI/CD integration
- [TypeScript SDK](https://developers.openai.com/codex/codex-sdk) - Programmatic usage
- [VS Code Extension](https://developers.openai.com/codex/ide) - IDE integration

**Related Tools:**
- [Kimi Cheat Sheet](https://github.com/BA-CalderonMorales/kimi-cheat-sheet) - Companion guide for Kimi Code CLI

**Model Context Protocol:**
- [MCP Specification](https://modelcontextprotocol.io/) - Official MCP protocol docs
- [MCP Server Examples](https://github.com/modelcontextprotocol/servers) - Community MCP servers

> **Tip**: Always check the [official Codex documentation](https://github.com/openai/codex) for the latest features and updates. This cheat sheet is a quick reference, but the official docs contain the most comprehensive and up-to-date information.

## Contributing

Found an issue or have a suggestion? Contributions are welcome!

- Report bugs or issues
- Suggest new examples
- Improve documentation
- Share your workflows

## License

This cheat sheet is provided under the Apache License 2.0.

## Credits and Inspiration

This cheat sheet was inspired by the excellent [claude-code-cheat-sheet](https://github.com/Njengah/claude-code-cheat-sheet) by @Njengah. We adapted their progressive learning structure to create a similar quick reference guide for OpenAI Codex CLI.

All commands and examples are verified against the [official OpenAI Codex documentation](https://developers.openai.com/codex).

**Last updated: July 2026**  
**Based on**: OpenAI Codex CLI (npm: @openai/codex)

---
*Last synced: 2026-07-19 via [workspace manager](https://github.com/BA-CalderonMorales)*
