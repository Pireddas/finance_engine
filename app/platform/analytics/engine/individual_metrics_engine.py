# individual_metrics_engine_v1.py
import numpy as np
from app.platform.analytics.metadata.manifests import individual_portfolio_manifest

class IndividualMetricsEngine:
    manifest = individual_portfolio_manifest()

    def metadata(self):
        return self.manifest

    def calculate(self, returns, risk_free_rate):       
        if len(returns) < 2:
            raise ValueError("Período insuficiente para métricas compostas")
        
        n_years = len(returns) / 252
        # Prevenção: evitar divisão por zero se o período for muito curto
        n_years = n_years if n_years > 0 else 1 

        total_returns = (1 + returns).prod() - 1
        cagr = ((1 + total_returns) ** (1 / n_years) - 1)

        excess_return = (returns.mean() * 252) - risk_free_rate
        volatility = returns.std() * np.sqrt(252)
        sharpe = excess_return / volatility.replace(0, np.nan)

        cum_rets = (1 + returns).cumprod()
        peak = cum_rets.cummax()
        drawdown = (cum_rets - peak) / peak

        return {
            "cagr": cagr.fillna(0).to_dict(),
            "sharpe": sharpe.fillna(0).to_dict(),
            "max_drawdown": drawdown.min().fillna(0).to_dict(),
            "volatility": volatility.fillna(0).to_dict()
        }
