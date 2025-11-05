<div align="center">

# Codex Cheat Sheet (Beta)

<img width="3840" height="1317" alt="image" src="https://github.com/user-attachments/assets/0749d33a-de10-4f1e-8ae7-492d61dc37a0" />

> **Your complete guide to mastering OpenAI Codex - from zero to hero in minutes!**

Ultimate collection of Codex tips, tricks, hacks, and workflows that you can use to master Codex CLI without having to remember every command.

**Based on official OpenAI Codex documentation** - All commands and examples are sourced from the [official Codex repository](https://github.com/openai/codex). For the most up-to-date information, always refer to the official docs.

</div>

## Quick Start

```bash
# Install with npm
npm install -g @openai/codex

# Or with Homebrew
brew install --cask codex

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
- **[Skills Integration (Advanced Setup)](#skills-integration-advanced-setup)** - Extensible, repeatable, shareable capabilities
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

# Update with npm
npm update -g @openai/codex

# Update with Homebrew
brew upgrade codex

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
/undo                     # Ask Codex to undo a turn
/diff                     # Show git diff (including untracked files)
/mention                  # Mention a file
/status                   # Show current session config and token usage
/mcp                      # List configured MCP tools
/logout                   # Log out of Codex
/quit                     # Exit Codex
/exit                     # Exit Codex
/feedback                 # Send logs to maintainers
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
model = "gpt-5"                    # Default model

# For reasoning models (o3, o4-mini, gpt-5, gpt-5-codex):
model_reasoning_effort = "medium"  # minimal, low, medium, high
model_reasoning_summary = "auto"   # auto, concise, detailed, none

# For GPT-5 family models:
model_verbosity = "medium"         # low, medium, high

# Models available:
# - gpt-5-codex (default on macOS/Linux)
# - gpt-5 (default on Windows)
# - o3, o4-mini (reasoning models)
# - Other OpenAI models via custom providers
```

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

See [MCP Documentation](https://github.com/openai/codex/blob/main/docs/config.md#mcp-integration) for details.

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

See [Sandbox & Approvals](https://github.com/openai/codex/blob/main/docs/sandbox.md) for details.

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

See [Non-Interactive Mode (exec)](https://github.com/openai/codex/blob/main/docs/exec.md) for details.

</details>

<details>
<summary><strong>Piping and Scripting</strong></summary>

```bash
# Pipe content to Codex
cat logs.txt | codex exec "find the error"

# Use in scripts
git diff | codex exec "create a commit message"

# Combine commands
codex exec "explain this file" < app.js > explanation.md
```

</details>

<details>
<summary><strong>Skills Integration (Advanced Setup)</strong></summary>

Skills allow you to create reusable, shareable capabilities that extend Codex's functionality. While Codex doesn't have built-in skills support yet (see [openai/codex#5291](https://github.com/openai/codex/issues/5291)), you can implement custom skills systems.

**Community Solutions:**

The [openskills](https://github.com/numman-ali/openskills) repository provides a framework for creating extensible, repeatable, and shareable skills for Codex. This approach allows you to:

- Define custom workflows and automations
- Share skills across projects and teams
- Build libraries of reusable capabilities
- Take full control of Codex in an extensible way

**Implementation Approaches:**

```bash
# Using custom prompts directory
~/.codex/prompts/
├── code-review.md
├── refactor-patterns.md
└── test-generation.md

# Using AGENTS.md for project-specific skills
# Define standard workflows and patterns in AGENTS.md
```

**Note:** This is an advanced setup that requires custom integration. Check the [Codex skills discussion](https://github.com/openai/codex/issues/5291) for updates on native skills support. If native skills support has been added since this guide was written, refer to the official documentation for the recommended approach.

See [Custom Prompts](https://github.com/openai/codex/blob/main/docs/prompts.md) for creating reusable prompt templates.

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
<summary><strong>TypeScript SDK</strong></summary>

```typescript
// Programmatic Codex usage
import { Codex } from '@openai/codex-sdk';

const codex = new Codex({
  apiKey: process.env.OPENAI_API_KEY
});

const response = await codex.exec({
  prompt: "Analyze this codebase",
  workingDirectory: "./src"
});

console.log(response.output);
```

See [TypeScript SDK](https://github.com/openai/codex/tree/main/sdk/typescript) for details.

</details>

<details>
<summary><strong>Automated Workflows</strong></summary>

```bash
# Code review automation
#!/bin/bash
git diff HEAD~1 | codex exec "review for bugs" > review.md

# Documentation generation
codex exec "generate API docs from comments" > API.md

# Test generation
codex exec "create tests for all functions in src/" > tests/

# Release notes
git log --oneline v1.0..HEAD | codex exec "create release notes" > RELEASE_NOTES.md
```

</details>

<details>
<summary><strong>Complex Prompts</strong></summary>

```bash
# Multi-step tasks
codex exec "
1. Analyze the codebase structure
2. Identify potential performance bottlenecks
3. Suggest specific optimizations
4. Create an implementation plan
"

# Contextual analysis
codex "Based on the AGENTS.md file, refactor this code to follow our standards"
```

</details>

<details>
<summary><strong>Zero Data Retention (ZDR)</strong></summary>

```bash
# ZDR is available for Enterprise customers
# Data is not used for training
# API requests not logged beyond 30 days
# Configure via your OpenAI Enterprise account settings

# For more info:
# See: https://github.com/openai/codex/blob/main/docs/zdr.md
```

</details>

## Command Reference

### CLI Commands

| Command | Description | Example |
|---------|-------------|---------|
| `codex` | Start interactive TUI | `codex` |
| `codex "prompt"` | Start with initial prompt | `codex "explain this"` |
| `codex exec "..."` | Non-interactive execution | `codex exec "analyze code"` |
| `codex resume` | Resume session (picker) | `codex resume` |
| `codex resume --last` | Resume most recent session | `codex resume --last` |
| `codex resume <ID>` | Resume specific session | `codex resume abc-123` |
| `codex --version` | Show version | `codex --version` |
| `codex --model <model>` | Use specific model | `codex --model gpt-5` |
| `codex --cd <dir>` | Set working directory | `codex --cd /path/to/project` |
| `codex --add-dir <dir>` | Add extra writable directory | `codex --add-dir ../backend` |

### Slash Commands

| Command | Description |
|---------|-------------|
| `/model` | Choose model and reasoning effort |
| `/approvals` | Configure approval settings |
| `/review` | Review current changes and find issues |
| `/new` | Start a new chat during conversation |
| `/init` | Create AGENTS.md file with instructions |
| `/compact` | Summarize conversation to prevent context limit |
| `/undo` | Ask Codex to undo a turn |
| `/diff` | Show git diff (including untracked files) |
| `/mention` | Mention a file |
| `/status` | Show session config and token usage |
| `/mcp` | List configured MCP tools |
| `/logout` | Log out of Codex |
| `/quit` | Exit Codex |
| `/exit` | Exit Codex |
| `/feedback` | Send logs to maintainers |

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Cancel operation |
| `Ctrl+D` | Exit Codex |
| `Tab` | Auto-complete |
| `↑/↓` | Command history |
| `Esc Esc` | Edit previous message (backtrack mode) |
| `@` | Trigger fuzzy file search |
| `Ctrl+V` / `Cmd+V` | Paste images into composer |

## Best Practices

<details>
<summary><strong>Effective Prompting</strong></summary>

**Do:**
- Be specific and clear
- Break complex tasks into steps
- Provide context in AGENTS.md
- Use slash commands for common tasks
- Review Codex's plan before approval

**Don't:**
- Give vague instructions
- Skip reviewing bash commands
- Ignore security warnings
- Over-rely on auto-approve

</details>

<details>
<summary><strong>Security Tips</strong></summary>

- Always review bash commands before approval
- Use `approval_policy = "untrusted"` to be prompted for risky commands
- Use `sandbox_mode = "read-only"` for analysis tasks
- Use `sandbox_mode = "workspace-write"` to limit writes to project directory
- Avoid `sandbox_mode = "danger-full-access"` unless in controlled environment
- Enable ZDR for Enterprise customers with sensitive projects
- Keep Codex updated for latest security features

</details>

<details>
<summary><strong>Performance Tips</strong></summary>

- Use `/compact` to summarize long conversations and free up context
- Use `/new` to start fresh chat within same session
- Create AGENTS.md files to provide project context once
- Use `codex exec` for automated, non-interactive workflows
- Configure MCP servers for extended capabilities
- Use profiles for different project types

</details>

<details>
<summary><strong>Project Organization</strong></summary>

```bash
# Recommended structure
project/
├── AGENTS.md              # Project context for Codex
├── .codex/
│   └── prompts/          # Custom prompts
├── src/                  # Source code
└── docs/                 # Documentation
```

</details>

<details>
<summary><strong>Team Collaboration</strong></summary>

- Share AGENTS.md in version control
- Create team-specific custom prompts
- Document Codex workflows in README
- Use consistent coding standards
- Review Codex-generated code together

</details>

## Common Use Cases

<details>
<summary><strong>Code Review</strong></summary>

```bash
codex "Review this PR for:
1. Security vulnerabilities
2. Performance issues
3. Code style violations
4. Test coverage"
```

</details>

<details>
<summary><strong>Debugging</strong></summary>

```bash
# Analyze error logs
cat error.log | codex exec "find the root cause"

# Debug specific function
codex "Debug why the login function is failing"
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
- [Getting Started Guide](https://github.com/openai/codex/blob/main/docs/getting-started.md) - Comprehensive getting started guide
- [Configuration Reference](https://github.com/openai/codex/blob/main/docs/config.md) - Complete config.toml reference
- [Slash Commands](https://github.com/openai/codex/blob/main/docs/slash_commands.md) - All slash commands explained
- [Non-Interactive Mode (exec)](https://github.com/openai/codex/blob/main/docs/exec.md) - Automation with codex exec
- [Authentication](https://github.com/openai/codex/blob/main/docs/authentication.md) - Authentication methods
- [Sandbox & Approvals](https://github.com/openai/codex/blob/main/docs/sandbox.md) - Security and sandboxing
- [AGENTS.md Documentation](https://github.com/openai/codex/blob/main/docs/agents_md.md) - Project instructions guide
- [MCP Integration](https://github.com/openai/codex/blob/main/docs/advanced.md#model-context-protocol-mcp) - MCP setup and usage
- [Custom Prompts](https://github.com/openai/codex/blob/main/docs/prompts.md) - Creating custom prompts
- [FAQ](https://github.com/openai/codex/blob/main/docs/faq.md) - Frequently asked questions

**Extensions & Integrations:**
- [GitHub Action](https://github.com/openai/codex-action) - CI/CD integration
- [TypeScript SDK](https://github.com/openai/codex/tree/main/sdk/typescript) - Programmatic usage
- [VS Code Extension](https://developers.openai.com/codex/ide) - IDE integration

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

This cheat sheet is provided under the MIT License.

## Credits and Inspiration

This cheat sheet was inspired by the excellent [claude-code-cheat-sheet](https://github.com/Njengah/claude-code-cheat-sheet) by @Njengah. We adapted their progressive learning structure to create a similar quick reference guide for OpenAI Codex CLI.

All commands and examples are verified against the [official OpenAI Codex documentation](https://github.com/openai/codex).

**Last updated**: November 2025  
**Based on**: OpenAI Codex CLI (npm: @openai/codex)
