#!/usr/bin/env python3
"""
Test script to reproduce and verify the formatting issue.
"""

import subprocess
import sys

def run_isort_check():
    """Run isort check on the specific files that were failing."""
    print("Running isort check on non-test files...")
    
    # Run isort check on the specific files mentioned in the issue
    result = subprocess.run([
        sys.executable, "-m", "isort", 
        "beetsplug/listenbrainz.py", 
        "beetsplug/bpd/gstplayer.py", 
        "--check"
    ], capture_output=True, text=True)
    
    print(f"Exit code: {result.returncode}")
    if result.stdout:
        print(f"STDOUT:\n{result.stdout}")
    if result.stderr:
        print(f"STDERR:\n{result.stderr}")
    
    return result.returncode == 0

def run_black_check():
    """Run black check on the specific files."""
    print("\nRunning black check on non-test files...")
    
    result = subprocess.run([
        sys.executable, "-m", "black", 
        "beetsplug/listenbrainz.py", 
        "beetsplug/bpd/gstplayer.py", 
        "--check"
    ], capture_output=True, text=True)
    
    print(f"Exit code: {result.returncode}")
    if result.stdout:
        print(f"STDOUT:\n{result.stdout}")
    if result.stderr:
        print(f"STDERR:\n{result.stderr}")
    
    return result.returncode == 0

def main():
    """Main test function."""
    print("Testing formatting issues...")
    
    isort_passed = run_isort_check()
    black_passed = run_black_check()
    
    print(f"\nResults:")
    print(f"isort check: {'PASSED' if isort_passed else 'FAILED'}")
    print(f"black check: {'PASSED' if black_passed else 'FAILED'}")
    
    if isort_passed and black_passed:
        print("\nAll formatting checks PASSED!")
        return 0
    else:
        print("\nSome formatting checks FAILED!")
        return 1

if __name__ == "__main__":
    sys.exit(main())