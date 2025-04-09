#!/usr/bin/env python3
"""
Test script to verify import sorting issues in the repository.
"""

import subprocess
import sys

def run_isort_check(paths):
    """Run isort check on the specified paths."""
    try:
        result = subprocess.run(
            ["isort", "--check"] + paths,
            capture_output=True,
            text=True,
            check=True
        )
        print("All imports are correctly sorted!")
        return True
    except subprocess.CalledProcessError as e:
        print("Import sorting issues found:")
        print(e.stderr)
        return False

if __name__ == "__main__":
    # Check the specific files mentioned in the issue
    files_to_check = [
        "beetsplug/edit.py",
        "beetsplug/bpd/gstplayer.py"
    ]
    
    success = run_isort_check(files_to_check)
    sys.exit(0 if success else 1)