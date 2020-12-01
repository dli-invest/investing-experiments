import pandas as pd
from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities
# Expects to be moved to ~/.zipline/extension.py
start_session = pd.Timestamp('2019-09-03', tz='utc')
end_session = pd.Timestamp('2020-11-27', tz='utc')

# register the bundle
register(
    'dcm_firstbt',  # name we select for the bundle
    csvdir_equities(
        # name of the directory as specified above (named after data frequency)
        ['daily'],
        # path to directory containing the
        '/root/workspace/zipline-experiments/data/tsx',
    ),
    calendar_name='XTSE',  # TSX
    start_session=start_session,
    end_session=end_session
)