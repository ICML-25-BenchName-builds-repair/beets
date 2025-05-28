#!/usr/bin/env python3
"""
Verification script to confirm that all non-test files pass isort check.
"""

import subprocess
import sys
import os

def verify_non_test_files():
    """Verify that all non-test files pass isort check."""
    print("=== Verifying Non-Test Files ===")
    
    # Change to the repository directory
    os.chdir('/lca-workspace/repos/beetbox__beets')
    
    # Check beets and beetsplug directories (non-test files)
    print("Checking beets and beetsplug directories...")
    result = subprocess.run(
        ['isort', 'beets', 'beetsplug', '--check'],
        capture_output=True,
        text=True
    )
    
    print(f"Exit code: {result.returncode}")
    if result.stdout:
        print(f"STDOUT:\n{result.stdout}")
    if result.stderr:
        print(f"STDERR:\n{result.stderr}")
    
    if result.returncode == 0:
        print("✅ All non-test files pass isort check!")
        return True
    else:
        print("❌ Some non-test files still have import sorting issues.")
        return False

def verify_specific_files():
    """Verify the specific files mentioned in the issue."""
    files_to_check = [
        'beetsplug/edit.py',
        'beetsplug/bpd/gstplayer.py'
    ]
    
    print("\n=== Verifying Specific Files ===")
    all_passed = True
    
    for file_path in files_to_check:
        print(f"Checking {file_path}...")
        result = subprocess.run(
            ['isort', file_path, '--check'],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"✅ {file_path} passes")
        else:
            print(f"❌ {file_path} fails")
            print(f"STDERR: {result.stderr}")
            all_passed = False
    
    return all_passed

if __name__ == "__main__":
    print("Verifying that the formatting issue has been resolved...")
    
    non_test_passed = verify_non_test_files()
    specific_passed = verify_specific_files()
    
    if non_test_passed and specific_passed:
        print("\n🎉 SUCCESS: All non-test files are properly formatted!")
        print("The CI formatting check should now pass for non-test files.")
        sys.exit(0)
    else:
        print("\n❌ FAILURE: Some files still need formatting fixes.")
        sys.exit(1)