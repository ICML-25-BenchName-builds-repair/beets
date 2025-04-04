#!/bin/bash
# Test script to verify isort formatting

echo "Running isort check on listenbrainz.py..."
python -m isort beetsplug/listenbrainz.py --check-only
if [ $? -eq 0 ]; then
    echo "✅ isort check passed!"
    exit 0
else
    echo "❌ isort check failed!"
    echo "Showing diff of what needs to be fixed:"
    python -m isort beetsplug/listenbrainz.py --diff
    exit 1
fi