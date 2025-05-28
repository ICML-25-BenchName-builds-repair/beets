#!/usr/bin/env python3
"""
Script to reproduce the formatting issue and verify the fix.
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

def test_formatting():
    """Test the formatting of the smartplaylist test file."""
    repo_root = Path(__file__).parent
    test_file = repo_root / "test" / "plugins" / "test_smartplaylist.py"
    
    print(f"Testing formatting for: {test_file}")
    
    # Test isort
    print("\n=== Testing isort ===")
    returncode, stdout, stderr = run_command(
        f"python -m isort {test_file} --check --diff", 
        cwd=repo_root
    )
    print(f"isort return code: {returncode}")
    if stdout:
        print("isort stdout:", stdout)
    if stderr:
        print("isort stderr:", stderr)
    
    # Test black
    print("\n=== Testing black ===")
    returncode, stdout, stderr = run_command(
        f"python -m black {test_file} --check --diff", 
        cwd=repo_root
    )
    print(f"black return code: {returncode}")
    if stdout:
        print("black stdout:", stdout)
    if stderr:
        print("black stderr:", stderr)
    
    # Test the full format_check command
    print("\n=== Testing full format_check (just this file) ===")
    returncode, stdout, stderr = run_command(
        f"python -m isort {test_file} --check && python -m black {test_file} --check", 
        cwd=repo_root
    )
    print(f"Combined format check return code: {returncode}")
    
    return returncode == 0

if __name__ == "__main__":
    success = test_formatting()
    if success:
        print("\n✅ All formatting checks passed!")
        sys.exit(0)
    else:
        print("\n❌ Formatting checks failed!")
        sys.exit(1)