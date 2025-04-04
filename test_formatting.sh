#!/bin/bash
cd /lca-workspace/repos/beetbox__beets
python -m black beetsplug/listenbrainz.py --check
if [ $? -ne 0 ]; then
    echo "Black formatting check failed"
    exit 1
fi

python -m isort beetsplug/listenbrainz.py --check
if [ $? -ne 0 ]; then
    echo "isort check failed"
    exit 1
fi

echo "All formatting checks passed!"
exit 0