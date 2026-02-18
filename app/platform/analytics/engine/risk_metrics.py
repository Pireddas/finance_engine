# app\platform\analytics\engine\risk_metrics.py

import numpy as np
import pandas as pd
from app.platform.analytics.metadata.manifests import tail_risk_manifest

class TailRiskEngine:
    manifest = tail_risk_manifest()

    def metadata(self):
        return self.manifest

    def calculate(self, returns: pd.Series):
        if isinstance(returns, pd.DataFrame):
            returns = returns.iloc[:, 0]

        returns = returns.dropna()

        confidences = [95, 98, 99, 99.9]
        results = {}

        for conf in confidences:
            percentile_val = 100 - conf
            var_val = np.percentile(returns, percentile_val)

            tail_returns = returns[returns <= var_val]
            cvar_val = tail_returns.mean() if not tail_returns.empty else var_val

            key = str(conf).replace(".", "_")
            results[f"var_{key}"] = float(var_val)
            results[f"cvar_{key}"] = float(cvar_val)

        results["worst_day"] = float(returns.min())
        results["daily_std"] = float(returns.std())

        mean_return = float(returns.mean())
        z_score = (
            (results["worst_day"] - mean_return) / results["daily_std"]
            if results["daily_std"] != 0
            else 0
        )

        results["z_score_worst"] = float(z_score)

        return results
