# correlation_engine_v1.py
import pandas as pd
from app.platform.analytics.metadata.manifests import correlation_portfolio_manifest

class CorrelationEngine:
    manifest = correlation_portfolio_manifest()

    def metadata(self):
        return self.manifest

    def calculate(self, returns: pd.DataFrame):
        corr_matrix = returns.corr(method=self.manifest["assumptions"]['method'])

        return corr_matrix.to_dict()
