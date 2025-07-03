#!/bin/bash
cd /lca-workspace/repos/beetbox__beets
isort beetsplug/edit.py --check
if [ $? -eq 0 ]; then
    echo "isort check passed!"
    exit 0
else
    echo "isort check failed!"
    exit 1
fi