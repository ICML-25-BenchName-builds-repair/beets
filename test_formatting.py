#!/usr/bin/env python3
"""Test script to verify formatting issues."""

import subprocess
import sys

def run_black_check():
    """Run black check on the listenbrainz.py file."""
    result = subprocess.run(
        ["python", "-m", "black", "beetsplug/listenbrainz.py", "--check"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("Black check failed:")
        print(result.stderr)
        return False
    return True

def main():
    """Main function."""
    if run_black_check():
        print("Black check passed!")
        return 0
    else:
        print("Black check failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())