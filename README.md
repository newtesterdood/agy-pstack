# pstack for Google Antigravity

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: Antigravity](https://img.shields.io/badge/Platform-Google%20Antigravity-4285F4.svg)](https://antigravity.google)
[![Upstream: cursor/plugins](https://img.shields.io/badge/Upstream-cursor%2Fplugins%2Fpstack-black.svg)](https://github.com/cursor/plugins/tree/main/pstack)

A clean, safe, and native port of Lauren Tan's ([@poteto](https://x.com/poteto)) **pstack** for **Google Antigravity**.

> *"If you want to go fast, go deep first. pstack helps you write less, but higher quality code. Rigorous agent workflows you can parallelize with confidence."* — Lauren Tan

This repository provides the full, unabridged collection of `pstack` workflows—including all 23 playbooks, 24 engineering principles, 54 specialized skills, and complete guides—engineered with seamless, native drop-in replacements for Google Antigravity.

---

## Key Features in this Port

1. **Complete Upstream Suite Intact**:
   - **All 23 Playbooks**: `bug-fix`, `feature`, `investigation`, `perf-issue`, `refactoring`, `prototype`, `shipping`, `multi-phase-plan`, `autonomous-run`, `orchestrate`, `autopilot-full`, and more.
   - **All 24 Principles**: `principle-laziness-protocol`, `principle-model-the-domain`, `principle-fix-root-causes`, `principle-prove-it-works`, `principle-attack-the-premise`, etc.
   - **All Situational Skills**: `architect`, `arena`, `swarm`, `interrogate`, `unslop`, `no-comments`, `technical-writing`, `tdd`, `how`, `why`, `poteto-help`.
   - **Full Documentation**: Complete 10-part engineering guide in `docs/guide/`.

2. **Native Antigravity Drop-In Replacements**:
   Instead of modifying upstream skill texts, this port uses a declarative harness (`rules/AGENTS.md` and `docs/harness/antigravity.md`):
   - **Subagents**: Replaces Cursor `Task` with native Antigravity `invoke_subagent` (mapping reasoning roles to `pro` and execution delegates to `flash`).
   - **Interactive Clarifications**: Replaces `AskQuestion` with Antigravity's native `ask_question` tool.
   - **Plans & Checklists**: Replaces `TodoWrite` with persistent Antigravity Markdown Artifacts (`/brain/...`).
   - **Safe Sandbox Execution**: Replaces unvetted host scripts with sandboxed, verified command execution.

3. **Built-in `pstack-update` Skill**:
   - Inspects GitHub for new versions and releases.
   - Prompts the user with `ask_question` before applying updates.
   - Automatically creates a timestamped archive backup (`.backups/pstack_backup_*.tar.gz`).
   - Validates configuration migrations and offers interactive adoption of new options.

4. **Built-in `pstack-sync` Skill**:
   - Compares Lauren Tan's official `cursor/plugins/pstack` against this `agy-pstack` repository.
   - Automatically detects upstream additions and synchronizes improvements.
   - Ensures Antigravity native drop-in replacements are permanently protected and wired in.

---

## Installation

### Workspace Level (Project-Specific)
Place or link this repository inside your workspace's `.agents/plugins/` directory:
```bash
mkdir -p .agents/plugins
ln -s /path/to/agy-pstack .agents/plugins/pstack
```

### Global Level (All Projects)
Clone or copy this repository to your global Antigravity plugins directory:
```bash
git clone https://github.com/your-username/agy-pstack.git ~/.gemini/config/plugins/pstack
```

---

## Quick Start

### 1. Launch Poteto Mode
In chat, activate `/poteto-mode` whenever starting a task that demands deep engineering rigor:
```text
/poteto-mode We have an intermittent race condition when synchronizing multi-agent worktrees. Root-cause first, then fix and verify with tests.
```

### 2. Need Help Choosing a Playbook?
Run `/poteto-help` to have the agent inspect your goal and recommend the exact playbook and principle.

### 3. Check for Updates
Run `/pstack-update` to check GitHub for updates, create an automated backup archive, and migrate configuration.

### 4. Sync Upstream (Maintainers)
Run `/pstack-sync` to compare against Lauren Tan's official `cursor/plugins/pstack` and audit all Antigravity drop-in replacements.

---

## Repository Structure

```text
.
├── plugin.json                 # Antigravity plugin manifest
├── LICENSE                     # MIT License
├── README.md                   # This documentation
├── UPSTREAM_README.md          # Upstream README from Lauren Tan
├── rules/
│   └── AGENTS.md               # Antigravity always-on rules (drop-in replacements & principles)
├── agents/
│   ├── poteto-agent.md         # Subagent definition for delegates
│   └── comment-sicko.md        # Comment audit agent
├── docs/
│   ├── guide/                  # 10-part deep engineering guide
│   └── harness/
│       ├── antigravity.md      # Official Antigravity harness adapter specification
│       └── claude-code.md      # Reference Claude Code harness adapter
└── skills/
    ├── poteto-mode/            # Main entry point & 23 playbooks
    ├── pstack-update/          # Update, backup archive, & migration skill
    ├── pstack-sync/            # Upstream sync & drop-in audit skill
    ├── principles/             # 24 core engineering principles
    └── ...                     # 54 complete upstream skills
```

---

## Attribution & License

- **Original Author**: [Lauren Tan](https://x.com/poteto) (Cursor / React Core Team).
- **Original Source**: [cursor/plugins/pstack](https://github.com/cursor/plugins/tree/main/pstack).
- **License**: [MIT License](LICENSE).
