#!/usr/bin/env python3
"""Test script to verify formatting issues."""

import subprocess
import sys

def main():
    """Run black check on listenbrainz.py and report results."""
    result = subprocess.run(
        ["black", "--check", "beetsplug/listenbrainz.py"],
        capture_output=True,
        text=True,
    )
    
    print("Exit code:", result.returncode)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    
    if result.returncode != 0:
        print("Formatting check failed!")
        return False
    else:
        print("Formatting check passed!")
        return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)