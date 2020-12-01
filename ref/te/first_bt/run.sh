#!/bin/sh

# get data
python3.6 data.py
cp ~/.zipline/extension.py ~/.zipline/extensionBackup.py
cp extension.py ~/.zipline/extension.py
# python3.6 main.py
zipline ingest -b dcm_firstbt
zipline run --start 2019-09-03 --end 2020-11-29 --capital-base 1000 --bundle dcm_firstbt --no-benchmark -f zp_dcm.py

