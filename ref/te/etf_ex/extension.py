import pandas as pd
import os
from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities
# Expects to be moved to ~/.zipline/extension.py
start_session = pd.Timestamp('2019-05-01', tz='utc')
end_session = pd.Timestamp('2020-12-10', tz='utc')

# register the bundle
register(
    'bt_tickers',  # name we select for the bundle
    csvdir_equities(
        # name of the directory as specified above (named after data frequency)
        ['daily'],
        # path to directory containing the
        '/home/vscode/workspace/zipline-experiments/data/etf',
    ),
    calendar_name='XTSE',  # TSX
    start_session=start_session,
    end_session=end_session
)