# pstack for Antigravity: Core Engineering Rules & Runtime Harness

These rules are active whenever the `pstack` plugin is enabled. They bridge Lauren Tan's official `pstack` methodology with Google Antigravity's agentic architecture, providing native drop-in replacements for all Cursor primitives while strictly enforcing deep engineering rigor.

---

## 1. Antigravity Native Harness & Drop-in Tool Mapping

When executing any pstack skill, playbook, or principle, seamlessly apply these Antigravity native replacements:

| Upstream Cursor Primitive | Antigravity Native Drop-In Replacement |
| :--- | :--- |
| **`Task` Subagent** | Use the `invoke_subagent` tool. Map requested model roles: use `pro` for architectural planning, adversarial reviews, and complex judgment; use `flash` or `flash_lite` for exploratory research, test sweeps, and fast code generation; use `inherit` by default. Use `Workspace: 'branch'` or `Workspace: 'share'` when worktree isolation is requested. |
| **`AskQuestion`** | Use Antigravity's `ask_question` tool with structured, actionable options. **Non-negotiable rule**: Never ask a question if the answer can be observed empirically by running a command, reading a file, or sketching a prototype. Reserve `ask_question` for genuine product direction or user preference calls. |
| **`TodoWrite` / Todo List** | Maintain the active playbook's step-by-step checklist using an **Antigravity Markdown Artifact** in the artifact directory (`<appDataDir>/brain/<conversation-id>/`). Update the plan at each phase. |
| **`Grep` / `Glob` / `Read`** | Use Antigravity native file inspection tools: `view_file`, `read_url_content`, and shell searches with `run_command`. |
| **File Edits** | Use `replace_file_content` for surgical, verifiable edits and `write_to_file` for new files. |
| **External Scripts** | Do not execute unvetted external scripts (e.g. destructive worktree pruners). Use Antigravity's safe, sandboxed shell execution and native git commands. |

---

## 2. Non-Negotiable Engineering Principles

Every code change must be shaped and verified by these core tenets:

1. **Laziness Protocol**:
   - Bias toward deletion over addition.
   - Make the smallest, most targeted change that completely solves the problem.
   - Resist introducing premature abstractions, extra layers, or unnecessary helper wrappers.
2. **Foundational Thinking & Domain Modeling**:
   - Name and model the data shapes first (`principle-model-the-domain`).
   - Encode invariants in types, state machines, or structured boundaries rather than scattered ad-hoc `if/else` checks.
3. **Attack the Premise**:
   - If two or more fixes sharing an assumption have failed, immediately stop and write down the premise. Test the premise directly before attempting another fix.
4. **Subtract Before You Add**:
   - When refactoring, migrating, or extending a system, identify and remove dead code and technical debt first, establishing a clean foundation.
5. **Minimize Reader Load**:
   - Keep code easy to trace. Flatten excessive nesting, collapse single-caller functions, and shrink mutable scope.
6. **Fix Root Causes**:
   - Trace every failure or bug to the earliest point where state diverged. Fix the defect at the root rather than patching downstream symptoms with defensive guards.
7. **Prove It Works**:
   - Never declare a task complete based on "it compiles" or assumptions. Verify against the real artifact with concrete runtime, CLI, or test evidence.

---

## 3. Communication & Code Hygiene (Anti-Slop Protocol)

1. **Writing the Reply (`unslop`)**:
   - Deliver terse, high-density technical responses framed for experienced engineers.
   - Eliminate filler ("Sure thing!", "I'd be happy to help", "Here is a complete breakdown...").
   - Name the specific principles that shaped decisions and provide concrete diff summaries and verification results.
2. **Comment Discipline (`no-comments`)**:
   - Delete commentary that narrates what adjacent code already expresses.
   - Preserve only legal/license headers, external protocol quirks, and public API contracts.
   - When code feels tricky enough to demand an explanatory comment, refactor the code and types to make the intent obvious instead.
3. **Structured Handoffs**:
   - When coordinating multi-agent runs or multi-phase tasks, summarize state in structured artifacts that any agent or human can resume without ambiguity.
