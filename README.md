# Codex Cheat Sheet

> **Your complete guide to mastering OpenAI Codex - from zero to hero in minutes!**

Ultimate collection of Codex tips, tricks, hacks, and workflows that you can use to master Codex CLI without having to remember every command.

## 🚀 Quick Start

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

## 📚 Table of Contents

- 🟢 **[Level 1: Getting Started](#-level-1-getting-started)**
- 🟡 **[Level 2: Basic Commands](#-level-2-basic-commands)**
- 🟠 **[Level 3: Intermediate Usage](#-level-3-intermediate-usage)**
- 🔴 **[Level 4: Advanced Features](#-level-4-advanced-features)**
- 🔵 **[Level 5: Expert Workflows](#-level-5-expert-workflows)**
- 📖 **[Command Reference](#-command-reference)**
- 💡 **[Best Practices](#-best-practices)**

---

## 🟢 Level 1: Getting Started

Essential commands to get you started with Codex.

### Installation

```bash
# Install globally with npm
npm install -g @openai/codex

# Install with Homebrew
brew install --cask codex

# Update with npm
npm update -g @openai/codex

# Update with Homebrew
brew upgrade codex
```

### First Steps

```bash
# Start interactive mode
codex

# Run with a specific prompt
codex "explain this project"

# Check installation health
codex /doctor

# View help
codex /help
```

### Authentication

```bash
# Sign in with ChatGPT account (recommended)
codex
# Then select "Sign in with ChatGPT"

# Use API key (alternative)
# Set OPENAI_API_KEY environment variable
export OPENAI_API_KEY="your-api-key"
```

### Basic Navigation

```bash
/help                     # Show all available commands
/exit                     # Exit Codex
Ctrl+C                    # Cancel current operation
Ctrl+D                    # Exit Codex
```

---

## 🟡 Level 2: Basic Commands

Core commands for everyday use.

### Slash Commands - Essentials

```bash
/help                     # Show available slash commands
/clear                    # Clear conversation history
/exit                     # Exit the REPL
/config                   # Open configuration panel
/doctor                   # Check system health
```

### File and Directory Operations

```bash
# Codex can read, write, and edit files
"Read the contents of src/app.js"
"Create a new file called utils.js"
"Edit the function in main.py to add error handling"

# View project structure
"Explain the structure of this project"
"What files are in the src directory?"
```

### Working with Code

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

### Session Management

```bash
# Continue working on previous task
codex --continue
codex -c

# View conversation history
# Codex maintains context within a session
```

---

## 🟠 Level 3: Intermediate Usage

Configuration and customization options.

### Configuration

```bash
# Config file location: ~/.codex/config.toml

# Open config file
codex /config

# Common configurations:
# - Default model
# - MCP servers
# - Custom prompts
# - Sandbox settings
```

### Model Selection

```bash
# Use specific model in config.toml
[model]
name = "gpt-4o"           # Default model
temperature = 0.7         # Creativity level (0.0-1.0)

# Models available:
# - gpt-4o (recommended)
# - gpt-4
# - gpt-3.5-turbo
```

### Custom Prompts

```bash
# Create custom prompts in ~/.codex/prompts/

# Example: Create ~/.codex/prompts/review.md
# Then use with:
"Use the review prompt on this code"
```

### Memory with AGENTS.md

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

---

## 🔴 Level 4: Advanced Features

Powerful features for advanced workflows.

### Model Context Protocol (MCP)

```bash
# Configure MCP servers in ~/.codex/config.toml

[[mcp_servers.filesystem]]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]

[[mcp_servers.github]]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-github"]
env = { GITHUB_TOKEN = "your-token" }

# MCP enables:
# - Filesystem access beyond current directory
# - Database connections
# - API integrations
# - Custom tool creation
```

### Sandbox & Permissions

```bash
# Codex runs in a sandbox by default
# You can approve/deny tool usage:
# - Bash commands
# - File operations
# - Network requests

# Configure in config.toml:
[sandbox]
auto_approve = ["bash:ls", "bash:cat", "bash:grep"]
auto_deny = ["bash:rm", "bash:sudo"]
```

### Non-Interactive Mode

```bash
# Execute and exit with codex exec
codex exec "summarize all TODO comments in this project"

# Useful for:
# - CI/CD pipelines
# - Automation scripts
# - Batch processing
```

### Piping and Scripting

```bash
# Pipe content to Codex
cat logs.txt | codex exec "find the error"

# Use in scripts
git diff | codex exec "create a commit message"

# Combine commands
codex exec "explain this file" < app.js > explanation.md
```

---

## 🔵 Level 5: Expert Workflows

Advanced patterns and automation.

### GitHub Actions Integration

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

### TypeScript SDK

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

### Automated Workflows

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

### Complex Prompts

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

### Zero Data Retention (ZDR)

```bash
# Enable ZDR for sensitive projects
# In config.toml:
[privacy]
zero_data_retention = true

# For Enterprise users - data not used for training
# Requests not logged beyond 30 days
```

---

## 📖 Command Reference

### CLI Commands

| Command | Description | Example |
|---------|-------------|---------|
| `codex` | Start interactive REPL | `codex` |
| `codex "prompt"` | Start with initial prompt | `codex "explain this"` |
| `codex exec "prompt"` | Non-interactive execution | `codex exec "analyze code"` |
| `codex --continue` | Continue last session | `codex -c` |
| `codex --version` | Show version | `codex --version` |

### Slash Commands

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/exit` | Exit Codex |
| `/clear` | Clear conversation history |
| `/config` | Open configuration |
| `/doctor` | Check system health |

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Cancel operation |
| `Ctrl+D` | Exit Codex |
| `Tab` | Auto-complete |
| `↑/↓` | Command history |

---

## 💡 Best Practices

### Effective Prompting

✅ **Do:**
- Be specific and clear
- Break complex tasks into steps
- Provide context in AGENTS.md
- Use slash commands for common tasks
- Review Codex's plan before approval

❌ **Don't:**
- Give vague instructions
- Skip reviewing bash commands
- Ignore security warnings
- Over-rely on auto-approve

### Security Tips

- Always review bash commands before approval
- Use sandbox auto_deny for dangerous commands
- Enable ZDR for sensitive projects
- Use API keys only when necessary
- Keep Codex updated

### Performance Tips

- Use `/clear` to reset context when switching tasks
- Create specific custom prompts for repeated tasks
- Use AGENTS.md to reduce repeated context
- Configure MCP servers for better access
- Use `codex exec` for automation

### Project Organization

```bash
# Recommended structure
project/
├── AGENTS.md              # Project context for Codex
├── .codex/
│   └── prompts/          # Custom prompts
├── src/                  # Source code
└── docs/                 # Documentation
```

### Team Collaboration

- Share AGENTS.md in version control
- Create team-specific custom prompts
- Document Codex workflows in README
- Use consistent coding standards
- Review Codex-generated code together

---

## 🎯 Common Use Cases

### Code Review

```bash
codex "Review this PR for:
1. Security vulnerabilities
2. Performance issues
3. Code style violations
4. Test coverage"
```

### Debugging

```bash
# Analyze error logs
cat error.log | codex exec "find the root cause"

# Debug specific function
codex "Debug why the login function is failing"
```

### Documentation

```bash
# Generate README
codex exec "Create a comprehensive README for this project"

# API documentation
codex exec "Generate API docs from JSDoc comments"

# Code comments
codex "Add detailed comments to this complex function"
```

### Testing

```bash
# Generate tests
codex "Create unit tests for all functions in utils.js"

# Test coverage
codex "Analyze test coverage and suggest missing tests"
```

### Refactoring

```bash
codex "Refactor this code to:
1. Improve readability
2. Add error handling
3. Follow TypeScript best practices
4. Add type definitions"
```

---

## 📚 Additional Resources

- [Official Documentation](https://github.com/openai/codex)
- [Getting Started Guide](https://github.com/openai/codex/blob/main/docs/getting-started.md)
- [Configuration Docs](https://github.com/openai/codex/blob/main/docs/config.md)
- [Slash Commands](https://github.com/openai/codex/blob/main/docs/slash_commands.md)
- [MCP Documentation](https://github.com/openai/codex/blob/main/docs/advanced.md#model-context-protocol-mcp)
- [GitHub Action](https://github.com/openai/codex-action)
- [TypeScript SDK](https://github.com/openai/codex/tree/main/sdk/typescript)
- [FAQ](https://github.com/openai/codex/blob/main/docs/faq.md)

---

## 🤝 Contributing

Found an issue or have a suggestion? Contributions are welcome!

- Report bugs or issues
- Suggest new examples
- Improve documentation
- Share your workflows

---

## 📄 License

This cheat sheet is provided under the MIT License.

## ⭐ Support

If this cheat sheet helped you:
- ⭐ Star this repository
- 📢 Share with other developers
- 💬 Provide feedback
- 🔄 Check for updates

---

**Last updated**: November 2025
**Based on**: OpenAI Codex CLI (npm: @openai/codex)
