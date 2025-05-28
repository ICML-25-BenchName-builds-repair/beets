#!/usr/bin/env python3
"""
Script to simulate the exact tox format_check commands.
"""

import subprocess
import sys
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a command and return the result."""
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=True, 
            text=True, 
            cwd=cwd
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)

def test_tox_format_check():
    """Test the exact commands that tox format_check runs."""
    repo_root = Path(__file__).parent
    
    print("Testing tox format_check commands...")
    
    # Test isort command from tox.ini
    print("\n=== Testing: isort beets beetsplug test --check ===")
    returncode, stdout, stderr = run_command(
        "python -m isort beets beetsplug test --check", 
        cwd=repo_root
    )
    print(f"isort return code: {returncode}")
    if returncode != 0:
        print("isort stdout:", stdout)
        print("isort stderr:", stderr)
        return False
    
    # Test black command from tox.ini
    print("\n=== Testing: black beets beetsplug test --check ===")
    returncode, stdout, stderr = run_command(
        "python -m black beets beetsplug test --check", 
        cwd=repo_root
    )
    print(f"black return code: {returncode}")
    if returncode != 0:
        print("black stdout:", stdout)
        print("black stderr:", stderr)
        return False
    
    return True

if __name__ == "__main__":
    success = test_tox_format_check()
    if success:
        print("\n✅ All tox format_check commands passed!")
        sys.exit(0)
    else:
        print("\n❌ tox format_check commands failed!")
        sys.exit(1)