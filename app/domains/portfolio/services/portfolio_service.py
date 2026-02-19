# app\domains\portfolio\services\portfolio_service.py

import json
from app.application.config import settings
from app.platform.analytics.engine.correlation_engine import CorrelationEngine
from app.platform.analytics.engine.individual_metrics_engine import IndividualMetricsEngine
from app.platform.analytics.engine.portfolio_metrics_engine import PortfolioMetricsEngine
from app.platform.analytics.engine.return_engine import ReturnEngine
from app.application.gpt.analyze_text import AnalyzeTextUseCase
from app.domains.portfolio.contract.prompt_contract import FinanceiroPromptContract

class PortfolioService:
  
    def __init__(
        self,
        market_data_repo,
        risk_free_rate: float | None = None,
        period: str | None = None,
    ):
        self.market_data_repo = market_data_repo
        self.rf_rate = risk_free_rate or settings.RISK_FREE_RATE
        self.period = period or settings.DATA_PERIOD

    def get_prices(
        self,
        tickers: list[str],
        start_date=None,
        end_date=None,
    ):
        return self.market_data_repo.fetch_data(
            tickers=tuple(tickers),
            start_date=start_date,
            end_date=end_date,
            period=self.period,
        )
 
    def get_portfolio_metrics(
        self, 
        tickers: list, 
        start_date: str = None, 
        end_date: str = None,
        ai_analysis: bool = False,
    ):

        tickers_tuple = tuple(sorted(tickers)) 

        df = self.market_data_repo.fetch_data(
            tickers=tickers_tuple,
            start_date=start_date,
            end_date=end_date,
        ) 

        if df is None:
            return {"error": "Um ou mais tickers são inválidos."}

        if df.empty:
            return {"error": "Dados insuficientes para o intervalo selecionado."}


        close_prices = df["Close"]

        returns_data = ReturnEngine().calculate(close_prices)
        returns = returns_data["returns"]

        correlation_data = CorrelationEngine().calculate(returns)

        individual = IndividualMetricsEngine().calculate(
            returns, settings.RISK_FREE_RATE
        )

        portfolio = PortfolioMetricsEngine().calculate(
            returns, settings.RISK_FREE_RATE
        )

        return {
            "results": {
                "portfolio": portfolio,
                "correlation_matrix": correlation_data,
                "individual_metrics": individual
                }
            }



        # close_prices = df["Close"]
        # returns = close_prices.pct_change().dropna()
        # # returns.to_parquet("./logs/df/df_portfolio.parquet")
        # # Cálculos Individuais (Pandas Series)
        # total_returns = (1 + returns).prod() - 1
        # n_years = len(returns) / 252
        # # Prevenção: evitar divisão por zero se o período for muito curto
        # n_years = n_years if n_years > 0 else 1 
        
        # individual_cagr = ((1 + total_returns) ** (1 / n_years) - 1).round(4)
        
        # excess_return_annual = (returns.mean() * 252) - settings.RISK_FREE_RATE
        # volatility_annual = returns.std() * np.sqrt(252)
        # individual_sharpe = (excess_return_annual / volatility_annual.replace(0, np.nan)).round(2)
        
        # # Max Drawdown
        # cum_rets = (1 + returns).cumprod()
        # peak = cum_rets.cummax()
        # drawdown = (cum_rets - peak) / peak
        # individual_max_drawdown = drawdown.min().round(4)

        # # Cálculos de Portfólio (Pesos Iguais)
        # weights = np.array([1/len(tickers)] * len(tickers))
        # cov_matrix = returns.cov() * 252
        # port_var = np.dot(weights.T, np.dot(cov_matrix, weights))
        # port_vol = np.sqrt(port_var)

        # # Cálculos de Portfólio (Continuação)
        # port_return = (returns.mean() * 252).dot(weights)
        # port_excess_return = port_return - settings.RISK_FREE_RATE
        # port_sharpe = (port_excess_return / port_vol).round(2)
        # port_cum = (1 + returns.dot(weights)).cumprod()
        # port_cagr = (port_cum.iloc[-1] ** (1 / n_years)) - 1
        
        # cagr = (port_cum.iloc[-1] ** (1 / n_years)) - 1

        # return {
        #     "results": {
        #         "portfolio": {
        #             "volatility": round(float(port_vol), 4),
        #             "sharpe": round(float(port_sharpe), 2),
        #             "expected_return": round(float(port_return), 4),
        #             "cagr": round(float(port_cagr), 4) 
        #         },
        #         "correlation_matrix": returns.corr().round(2).to_dict(),
        #         "individual_metrics": {
        #             "cagr": individual_cagr.fillna(0).to_dict(),
        #             "sharpe": individual_sharpe.fillna(0).to_dict(),
        #             "max_drawdown": individual_max_drawdown.fillna(0).to_dict(),
        #             "volatility": (returns.std() * np.sqrt(252)).round(4).fillna(0).to_dict()
        #         }
        #     }
        # }
