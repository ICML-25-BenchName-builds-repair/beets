#!/usr/bin/env python3
"""Script to verify that our changes will fix the CI workflow."""

import subprocess
import sys

def run_command(command):
    """Run a command and return the result."""
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=True,
    )
    return result

def main():
    """Main function."""
    # Check if black would reformat listenbrainz.py
    black_result = run_command("python -m black beetsplug/listenbrainz.py --check")
    if black_result.returncode != 0:
        print("Black check failed for listenbrainz.py:")
        print(black_result.stderr)
        return 1
    
    # Check if isort would reformat listenbrainz.py
    isort_result = run_command("python -m isort beetsplug/listenbrainz.py --check")
    if isort_result.returncode != 0:
        print("Isort check failed for listenbrainz.py:")
        print(isort_result.stderr)
        return 1
    
    print("All checks passed for listenbrainz.py!")
    print("The CI workflow should now pass.")
    return 0

if __name__ == "__main__":
    sys.exit(main())