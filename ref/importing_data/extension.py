import pandas as pd
from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities
# Expects to be moved to ~/.zipline/extension.py
start_session = pd.Timestamp('2017-01-02', tz='utc')
end_session = pd.Timestamp('2017-12-29', tz='utc')

# register the bundle
register(
    'eu_stocks',  # name we select for the bundle
    csvdir_equities(
        # name of the directory as specified above (named after data frequency)
        ['daily'],
        # path to directory containing the
        '/root/workspace/zipline-experiments/data/european',
    ),
    calendar_name='XAMS',  # Euronext Amsterdam
    start_session=start_session,
    end_session=end_session
)