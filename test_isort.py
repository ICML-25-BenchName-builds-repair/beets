#!/usr/bin/env python3
"""
Simple script to test isort formatting on the listenbrainz.py file.
"""

import subprocess
import sys

def main():
    """Run isort check on listenbrainz.py and report results."""
    print("Running isort check on beetsplug/listenbrainz.py...")
    
    try:
        result = subprocess.run(
            ["isort", "beetsplug/listenbrainz.py", "--check-only"],
            capture_output=True,
            text=True,
        )
        
        if result.returncode == 0:
            print("SUCCESS: Imports are correctly sorted.")
            return 0
        else:
            print("ERROR: Imports are incorrectly sorted.")
            print(result.stderr)
            return 1
    except Exception as e:
        print(f"Error running isort: {e}")
        return 2

if __name__ == "__main__":
    sys.exit(main())