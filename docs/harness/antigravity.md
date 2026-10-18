# pstack in Google Antigravity

This document defines the formal harness adapter specification for running Lauren Tan's **pstack** inside **Google Antigravity**.

`pstack` skills natively reference Cursor conventions. In Google Antigravity, this harness specification and the bundled `rules/AGENTS.md` automatically map Cursor primitives to Antigravity's native agentic architecture.

---

## 1. Tool Mappings

| Cursor Primitive | Google Antigravity Native Tool | Behavior & Notes |
| :--- | :--- | :--- |
| `Task` | `invoke_subagent` | Dispatches specialized subagents with dedicated prompts, roles, and model tiers. |
| `AskQuestion` | `ask_question` | Renders interactive modal questions with structured options. Follows pstack rule: observe empirically first before asking user. |
| `TodoWrite` / Todo List | Antigravity Markdown Artifacts | Created in `<appDataDir>/brain/<conversation-id>/` to track plan phases, checklists, and decisions. |
| `Read` / `View` | `view_file` | Direct read tool supporting slice ranges and binary inspection. |
| `Edit` | `replace_file_content` | Precise targeted substring replacement with strict whitespace matching. |
| `Write` / `New File` | `write_to_file` | Creates new files or overwrites existing ones. |
| `Grep` / `Glob` | `run_command` (`rg`, `find`) / file tools | High-speed code searches in the workspace sandbox. |
| `Bash` / Terminal | `run_command` | Sandboxed command execution with background task management via `manage_task`. |

---

## 2. Subagent & Model Mappings

When a pstack playbook delegates tasks to subagents:

### Tool Call: `invoke_subagent`

```json
{
  "Subagents": [
    {
      "Role": "Code Architect",
      "TypeName": "self",
      "Model": "pro",
      "Workspace": "inherit",
      "Prompt": "Perform parallel design exploration..."
    }
  ]
}
```

### Model Tier Translations (`pstack-models.mdc`)

In Cursor, model assignments are configured via `pstack-models.mdc`. In Antigravity, this is handled automatically via `rules/AGENTS.md`:

| Upstream Cursor Model Spec | Antigravity Native Model Tier |
| :--- | :--- |
| `claude-opus-5-5-xhigh`, `reasoning: max` | `pro` (Gemini Pro - deep reasoning, multi-turn architecture, complex judgment) |
| `grok`, code delegate, fast review | `flash` (Gemini Flash - rapid code generation, test sweeps, inspection) |
| `auto`, `inherit-parent` | `inherit` (default to current active model) |

### Workspace Isolation & `cloud_worktree`

Cursor's `cloud_worktree` and git worktree isolation map directly to Antigravity workspace modes:

| Cursor Environment Flag | Antigravity Workspace Parameter |
| :--- | :--- |
| `environment: "cloud"`, `cloud_worktree` | `Workspace: "branch"` (isolated branched workspace) |
| `isolation: "worktree"` | `Workspace: "share"` (shared worktree repository) |
| `environment: "local"` | `Workspace: "inherit"` (standard project workspace) |

---

## 3. Playbook Workflow with Antigravity Artifacts

When `/poteto-mode` activates:
1. The agent selects the matching playbook from `skills/poteto-mode/playbooks/`.
2. The agent creates a Markdown plan artifact using `write_to_file` in `<appDataDir>/brain/<conversation-id>/`.
3. As tasks advance, the artifact is updated with checked items `[x]` and verifiable diff links.
4. When multiple subagents fan out, each subagent reports back asynchronously; Antigravity's reactive wakeup resumes the orchestrator without polling loops.

---

## 4. Security & Sandbox Invariants

1. **No Unvetted Node/Bun Binaries**: Destructive or unvetted scripts (e.g. `worktree-audit.sh` or automated PR watchers) are replaced with native Git commands executed within Antigravity's safe sandbox.
2. **Audit Trails**: Long-running or overnight tasks maintain decision logs via `skills/show-me-your-work/` stored as persistent artifacts.
