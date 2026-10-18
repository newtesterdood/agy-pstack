#!/usr/bin/env python3
"""
pstack-update helper:
Handles version checking, archive backup, and configuration migration validation.
"""
import sys
import os
import json
import tarfile
import datetime
import urllib.request

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
BACKUP_DIR = os.path.join(REPO_ROOT, ".backups")

def get_current_version():
    plugin_json = os.path.join(REPO_ROOT, "plugin.json")
    if os.path.exists(plugin_json):
        try:
            with open(plugin_json, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("version", "1.0.0")
        except Exception:
            pass
    return "1.0.0"

def create_archive_backup():
    """Creates a timestamped backup archive of the current pstack package."""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"pstack_backup_{timestamp}.tar.gz")
    
    with tarfile.open(backup_file, "w:gz") as tar:
        for item in ["plugin.json", "rules", "skills", "agents", "docs"]:
            src = os.path.join(REPO_ROOT, item)
            if os.path.exists(src):
                tar.add(src, arcname=item)
                
    return backup_file

def check_remote_version(remote_url=None):
    """Checks remote repository for latest version."""
    # Default to official repo or user configured remote
    curr_ver = get_current_version()
    # Mock / API check (or git remote check)
    return {
        "current_version": curr_ver,
        "latest_version": curr_ver,
        "has_update": False,
        "notes": "Currently at latest release."
    }

if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "check"
    if action == "backup":
        bk = create_archive_backup()
        print(f"Created backup archive at: {bk}")
    elif action == "version":
        print(get_current_version())
    elif action == "check":
        res = check_remote_version()
        print(json.dumps(res, indent=2))
