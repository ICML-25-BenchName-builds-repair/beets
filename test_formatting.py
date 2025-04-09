#!/usr/bin/env python3
"""
Test script to verify formatting issues with Black.
"""

import subprocess
import sys

def run_black_check(file_path):
    """Run black --check on the specified file."""
    try:
        result = subprocess.run(
            ["black", file_path, "--check"],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            print(f"✅ {file_path} is properly formatted according to Black.")
            return True
        else:
            print(f"❌ {file_path} is not properly formatted according to Black.")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"Error running Black: {e}")
        return False

def run_isort_check(file_path):
    """Run isort --check on the specified file."""
    try:
        result = subprocess.run(
            ["isort", file_path, "--check"],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            print(f"✅ {file_path} imports are properly sorted according to isort.")
            return True
        else:
            print(f"❌ {file_path} imports are not properly sorted according to isort.")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"Error running isort: {e}")
        return False

def main():
    """Main function to run the formatting checks."""
    file_path = "beetsplug/listenbrainz.py"
    
    isort_result = run_isort_check(file_path)
    black_result = run_black_check(file_path)
    
    if isort_result and black_result:
        print("All formatting checks passed!")
        return 0
    else:
        print("Some formatting checks failed.")
        return 1

if __name__ == "__main__":
    sys.exit(main())