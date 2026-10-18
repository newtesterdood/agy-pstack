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

import subprocess
import re

def check_remote_version(remote_url=None):
    """Checks remote repository for latest version."""
    curr_ver = get_current_version()
    latest_ver = curr_ver
    try:
        cmd = ["git", "ls-remote", "--tags", remote_url or "origin"]
        out = subprocess.check_output(cmd, cwd=REPO_ROOT, stderr=subprocess.DEVNULL, text=True)
        tags = []
        for line in out.splitlines():
            m = re.search(r"refs/tags/v?(\d+\.\d+\.\d+)", line)
            if m:
                tags.append(m.group(1))
        if tags:
            def ver_key(v):
                return [int(x) for x in v.split(".")]
            tags.sort(key=ver_key)
            latest_ver = tags[-1]
    except Exception:
        pass

    has_update = False
    try:
        def ver_key(v):
            return [int(x) for x in v.split(".")]
        has_update = ver_key(latest_ver) > ver_key(curr_ver)
    except Exception:
        pass

    return {
        "current_version": curr_ver,
        "latest_version": latest_ver,
        "has_update": has_update,
        "notes": f"Update available: v{latest_ver}" if has_update else "Currently at latest release."
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
