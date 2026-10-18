---
name: pstack-update
description: Check for updates to pstack for Antigravity on GitHub, prompt the user to confirm, create an archive backup, update the plugin, and validate configuration migration options. Use for /pstack-update or when checking for pstack updates.
---

# pstack-update

Checks the GitHub repository for updates to this `pstack` Antigravity port, safely creates a backup archive before updating, migrates configuration options, and prompts the user for validation.

---

## Workflow Steps

### Step 1: Check Remote Repository for Updates
1. Read the current version from `plugin.json`.
2. Inspect the remote git repository or releases via `git fetch` or GitHub API to check for newer commits or releases.
3. Compare local commit/version with remote.

### Step 2: Confirm with User
If an update is found:
- Use the **`ask_question`** tool to prompt the user:
  - Question: "A newer version of pstack (vX.Y.Z) is available. Would you like to create a backup and update now?"
  - Options:
    - `(Recommended) Update pstack and create backup archive`
    - `Skip update and keep current version`
- If no update is found, report that pstack is currently up to date.

### Step 3: Create Archive Backup
Before modifying any files:
1. Run `python3 skills/pstack-update/scripts/update.py backup` or create a tarball archive of the existing configuration:
   - Target: `.backups/pstack_backup_<timestamp>.tar.gz`
   - Archive includes: `plugin.json`, `rules/`, `skills/`, `agents/`, `docs/`.
2. Confirm the archive path to the user.

### Step 4: Apply Update
1. Fast-forward git changes or unpack the release bundle into the workspace.
2. Verify integrity of all skill and rule files.

### Step 5: Configuration Migration & Validation
1. Compare the new `plugin.json` and `rules/AGENTS.md` against previous versions.
2. If new configuration toggles, model mappings, or suggested prompts were added:
   - Use `ask_question` to ask the user if they wish to customize the new settings or retain the defaults.
3. Present a clear summary of updated skills, new playbooks, and verified migrations.
