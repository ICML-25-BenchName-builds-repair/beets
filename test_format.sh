#!/bin/bash
cd /lca-workspace/repos/beetbox__beets
isort beetsplug/listenbrainz.py --check
if [ $? -eq 0 ]; then
    echo "Formatting check passed!"
    exit 0
else
    echo "Formatting check failed!"
    exit 1
fi