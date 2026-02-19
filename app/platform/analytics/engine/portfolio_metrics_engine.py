# portfolio_metrics_engine_v1.py
import numpy as np
from app.platform.analytics.metadata.manifests import portifolio_manifest

class PortfolioMetricsEngine:
    manifest = portifolio_manifest()

    def metadata(self):
        return self.manifest

    def calculate(self, returns, risk_free_rate):
        n_assets = returns.shape[1]
        weights = np.array([1 / n_assets] * n_assets)

        cov = returns.cov() * 252
        port_vol = np.sqrt(weights.T @ cov @ weights)

        port_return = (returns.mean() * 252).dot(weights)
        port_excess = port_return - risk_free_rate
        sharpe = port_excess / port_vol if port_vol != 0 else 0

        if len(returns) < 2:
            raise ValueError("Período insuficiente para métricas compostas")

        n_years = len(returns) / 252
        # Prevenção: evitar divisão por zero se o período for muito curto
        n_years = n_years if n_years > 0 else 1 
        port_cum = (1 + returns.dot(weights)).cumprod()
        cagr = (port_cum.iloc[-1] ** (1 / n_years)) - 1

        return {
            "volatility": (float(port_vol)),
            "expected_return": (float(port_return)),
            "sharpe": (float(sharpe)),
            "cagr": (float(cagr))
        } 
