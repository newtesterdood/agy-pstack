---
name: pstack-sync
description: Maintainer skill to compare Lauren Tan's upstream pstack repository against this agy-pstack repository, synchronize upstream improvements, and wire in native Antigravity drop-in replacements.
---

# pstack-sync

Maintains synchronization between Lauren Tan's upstream `pstack` ([cursor/plugins/pstack](https://github.com/cursor/plugins/tree/main/pstack)) and this `agy-pstack` port, ensuring all Antigravity native drop-in replacements remain seamlessly wired.

---

## Synchronization Workflow

### 1. Fetch Upstream Manifest & Diff
1. Fetch the latest `pstack/` tree from `https://github.com/cursor/plugins.git`.
2. Compare upstream files against local `agy-pstack`:
   - New upstream playbooks or skills
   - Modifications to existing playbooks, principles, or docs
   - New upstream references or templates

### 2. Guard Antigravity Native Replacements
Never allow upstream sync to overwrite Antigravity harness files:
- `plugin.json` (Antigravity plugin manifest)
- `rules/AGENTS.md` (active Antigravity drop-in rules)
- `docs/harness/antigravity.md` (Antigravity harness adapter spec)
- `skills/pstack-update/` (update skill)
- `skills/pstack-sync/` (sync skill)
- `README.md` (Antigravity documentation)

### 3. Wire Antigravity Drop-In Replacements
Whenever an upstream update introduces new tool references or primitives:
- Verify that `rules/AGENTS.md` and `docs/harness/antigravity.md` map them cleanly to Antigravity native tools:
  - Cursor `Task` -> `invoke_subagent`
  - Cursor `AskQuestion` -> `ask_question`
  - Cursor `TodoWrite` -> Antigravity Artifacts
  - Cursor `Grep`/`Glob` -> `view_file` / native search
- If a new primitive is found that lacks an Antigravity mapping, update `rules/AGENTS.md` and `docs/harness/antigravity.md` before applying the update.

### 4. Interactive Review & Execution
1. Present a clear diff summary showing:
   - Upstream files to update
   - Newly added skills or playbooks
   - Verification of drop-in replacements
2. Use **`ask_question`** to get user confirmation before committing the synced tree.
