# return_engine_v1.py
import pandas as pd
import numpy as np
from app.platform.analytics.metadata.manifests import return_portfolio_manifest

class ReturnEngine:
    manifest = return_portfolio_manifest()

    def metadata(self):
        return self.manifest

    def calculate(self, close_prices: pd.DataFrame):
        returns = close_prices.pct_change().dropna()

        return {
            "returns": returns,
        }
