#!/bin/bash
# Test script to verify that the formatting issue is fixed

# Check if isort is installed
if ! command -v isort &> /dev/null; then
    echo "isort is not installed. Installing..."
    pip install isort
fi

# Run isort check on the specific file
echo "Running isort check on beetsplug/edit.py..."
isort beetsplug/edit.py --check

# Check the exit code
if [ $? -eq 0 ]; then
    echo "✅ isort check passed for beetsplug/edit.py"
    exit 0
else
    echo "❌ isort check failed for beetsplug/edit.py"
    exit 1
fi