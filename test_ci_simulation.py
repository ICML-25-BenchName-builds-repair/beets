#!/usr/bin/env python3
"""
Simulate the exact CI commands that were failing.
"""

import subprocess
import sys

def simulate_ci_format_check():
    """Simulate the exact CI format_check commands."""
    print("Simulating CI format_check commands...")
    
    # First command: isort check
    print("\n1. Running: isort beets beetsplug test --check")
    result1 = subprocess.run([
        sys.executable, "-m", "isort", 
        "beets", "beetsplug", "test", "--check"
    ], capture_output=True, text=True)
    
    print(f"Exit code: {result1.returncode}")
    if result1.stdout:
        print(f"STDOUT:\n{result1.stdout}")
    if result1.stderr:
        print(f"STDERR:\n{result1.stderr}")
    
    # Second command: black check (only if first passes)
    if result1.returncode == 0:
        print("\n2. Running: black beets beetsplug test --check")
        result2 = subprocess.run([
            sys.executable, "-m", "black", 
            "beets", "beetsplug", "test", "--check"
        ], capture_output=True, text=True)
        
        print(f"Exit code: {result2.returncode}")
        if result2.stdout:
            print(f"STDOUT:\n{result2.stdout}")
        if result2.stderr:
            print(f"STDERR:\n{result2.stderr}")
        
        return result2.returncode == 0
    else:
        print("\n2. Skipping black check due to isort failure")
        return False

def main():
    """Main test function."""
    print("Testing CI format_check simulation...")
    
    success = simulate_ci_format_check()
    
    print(f"\nCI format_check simulation: {'PASSED' if success else 'FAILED'}")
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())