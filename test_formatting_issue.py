#!/usr/bin/env python3
"""
Reproduction script for the formatting check issue.
This script reproduces the exact issue mentioned in the CI failure.
"""

import subprocess
import sys
import os

def run_isort_check():
    """Run the isort check command that's failing in CI."""
    print("Running isort check command...")
    print("Command: isort beets beetsplug test --check")
    
    # Change to the repository directory
    os.chdir('/lca-workspace/repos/beetbox__beets')
    
    # Run the isort command
    result = subprocess.run(
        ['isort', 'beets', 'beetsplug', 'test', '--check'],
        capture_output=True,
        text=True
    )
    
    print(f"Exit code: {result.returncode}")
    print(f"STDOUT:\n{result.stdout}")
    print(f"STDERR:\n{result.stderr}")
    
    return result.returncode == 0

def check_specific_file():
    """Check the specific file mentioned in the issue."""
    print("\nChecking beetsplug/edit.py specifically...")
    
    result = subprocess.run(
        ['isort', 'beetsplug/edit.py', '--check'],
        capture_output=True,
        text=True
    )
    
    print(f"Exit code: {result.returncode}")
    print(f"STDOUT:\n{result.stdout}")
    print(f"STDERR:\n{result.stderr}")
    
    return result.returncode == 0

def show_diff():
    """Show what changes isort would make."""
    print("\nShowing diff for beetsplug/edit.py...")
    
    result = subprocess.run(
        ['isort', 'beetsplug/edit.py', '--diff'],
        capture_output=True,
        text=True
    )
    
    print(f"Diff output:\n{result.stdout}")

if __name__ == "__main__":
    print("=== Formatting Issue Reproduction Script ===")
    
    # Test the full command that's failing
    success = run_isort_check()
    
    # Test the specific file
    file_success = check_specific_file()
    
    # Show what needs to be fixed
    show_diff()
    
    print(f"\nResults:")
    print(f"Full isort check passed: {success}")
    print(f"beetsplug/edit.py check passed: {file_success}")
    
    if not success:
        print("\nThe issue is reproduced! The formatting check is failing.")
        sys.exit(1)
    else:
        print("\nNo formatting issues found.")
        sys.exit(0)