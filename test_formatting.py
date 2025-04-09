#!/usr/bin/env python3
"""Test script to verify formatting issues."""

import subprocess
import sys

def check_formatting():
    """Check if the file passes black formatting."""
    try:
        result = subprocess.run(
            ["black", "--check", "--line-length", "80", "beetsplug/listenbrainz.py"],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print("Formatting check failed:")
            print(result.stderr)
            return False
        return True
    except Exception as e:
        print(f"Error running black: {e}")
        return False

if __name__ == "__main__":
    if check_formatting():
        print("Formatting check passed!")
        sys.exit(0)
    else:
        print("Formatting check failed!")
        sys.exit(1)