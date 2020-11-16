import os
from zipline.utils.run_algo import load_extensions

load_extensions(
    default=True,
    extensions=[],
    strict=True,
    environ=os.environ,
)

from zipline.data import bundles

bundle = bundles.load('eu_stocks')
data = bundle.asset_finder.retrieve_all(bundle.asset_finder.sids)
print(data)