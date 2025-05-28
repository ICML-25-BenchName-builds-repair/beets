#!/usr/bin/env python3
"""
Verify that the specific issue mentioned in the problem description is fixed.
"""

import subprocess
import sys

def verify_specific_file_fix():
    """Verify that beetsplug/listenbrainz.py is no longer causing isort errors."""
    print("Verifying fix for beetsplug/listenbrainz.py...")
    
    # Check the specific file mentioned in the issue
    result = subprocess.run([
        sys.executable, "-m", "isort", 
        "beetsplug/listenbrainz.py", "--check", "-v"
    ], capture_output=True, text=True)
    
    print(f"Exit code: {result.returncode}")
    if result.stdout:
        print(f"STDOUT:\n{result.stdout}")
    if result.stderr:
        print(f"STDERR:\n{result.stderr}")
    
    return result.returncode == 0

def verify_no_listenbrainz_in_errors():
    """Verify that listenbrainz.py is not in the error list when running full check."""
    print("\nVerifying beetsplug/listenbrainz.py is not in error list...")
    
    result = subprocess.run([
        sys.executable, "-m", "isort", 
        "beets", "beetsplug", "test", "--check"
    ], capture_output=True, text=True)
    
    # Check if listenbrainz.py is mentioned in the errors
    listenbrainz_mentioned = "beetsplug/listenbrainz.py" in result.stderr
    
    print(f"listenbrainz.py mentioned in errors: {listenbrainz_mentioned}")
    
    return not listenbrainz_mentioned

def main():
    """Main verification function."""
    print("Verifying that the specific issue mentioned in the problem description is fixed...")
    
    file_check_passed = verify_specific_file_fix()
    not_in_errors = verify_no_listenbrainz_in_errors()
    
    print(f"\nResults:")
    print(f"beetsplug/listenbrainz.py isort check: {'PASSED' if file_check_passed else 'FAILED'}")
    print(f"beetsplug/listenbrainz.py not in error list: {'PASSED' if not_in_errors else 'FAILED'}")
    
    if file_check_passed and not_in_errors:
        print("\n✅ SUCCESS: The specific issue mentioned in the problem description has been FIXED!")
        print("The file beetsplug/listenbrainz.py now passes isort formatting checks.")
        return 0
    else:
        print("\n❌ FAILURE: The specific issue has not been resolved.")
        return 1

if __name__ == "__main__":
    sys.exit(main())