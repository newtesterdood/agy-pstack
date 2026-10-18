# Contributing to pstack for Google Antigravity

Thank you for your interest in contributing to **pstack for Google Antigravity** (`agy-pstack`).

This project is a community-driven open-source port of Lauren Tan's ([@poteto](https://x.com/poteto)) upstream [`cursor/plugins/pstack`](https://github.com/cursor/plugins/tree/main/pstack). To ensure respect for the original author and maintain clean upstream synchronizability, please follow these guidelines.

---

## 1. Where Does Your Contribution Belong?

### 🟢 Upstream to Lauren Tan's `cursor/plugins/pstack`
If your contribution touches core software engineering methodology, please submit a Pull Request directly to the official upstream repository:
- **Core Playbooks**: Changes, additions, or refinements in `skills/poteto-mode/playbooks/`
- **Core Principles**: New or improved principles in `skills/principle-*/`
- **Universal Skills & Guides**: Enhancements to `architect`, `interrogate`, `reflect`, `unslop`, or `docs/guide/`

Once merged upstream, our maintainer skill (`/pstack-sync`) will cleanly pull your improvements into this Antigravity port while preserving all runtime adapters.

### 🔵 To This Repository (`agy-pstack`)
Contributions to this repository should focus specifically on the **Google Antigravity platform integration**:
- **Harness Adapters**: Improvements to `rules/AGENTS.md` and `docs/harness/antigravity.md`
- **Tool Mapping**: Enhancements to how Cursor primitives map to Antigravity tools (`invoke_subagent`, `ask_question`, Markdown Artifacts)
- **Packaging & Skills**: Fixes or improvements to `skills/pstack-update` and `skills/pstack-sync`
- **Bug Fixes**: Platform-specific execution issues inside the Antigravity environment

---

## 2. Guiding Principles for PRs

1. **Preserve Upstream File Purity**:
   - Never mutate upstream skill markdown files with regex scripts to replace Cursor keywords.
   - All Antigravity translations must remain declarative within `rules/AGENTS.md` and harness documentation.
2. **Laziness Protocol**:
   - Bias toward deletion over addition. Make the smallest, cleanest change that completely solves the issue.
3. **No Slop**:
   - Keep code, types, and docs concise. Zero explanatory commentary narrating what adjacent code already expresses.

---

## 3. License & Attribution

All contributions to this repository are licensed under the [MIT License](LICENSE) and must preserve copyright attribution to Lauren Tan and original contributors.
