# app\domains\portfolio\services\portfolio_service.py

import json, os
import pandas as pd
from typing import Any
from app.application.config import settings
from app.platform.analytics.engine.correlation_engine import CorrelationEngine
from app.platform.analytics.engine.individual_metrics_engine import IndividualMetricsEngine
from app.platform.analytics.engine.portfolio_metrics_engine import PortfolioMetricsEngine
from app.platform.analytics.engine.return_engine import ReturnEngine
from app.application.gpt.analyze_text import AnalyzeTextUseCase
from app.domains.portfolio.contract.prompt_contract import FinanceiroPromptContract
from app.application.assemblers.portfolio_assembler import PortfolioMetricsResponseAssembler
from fastapi.encoders import jsonable_encoder

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
        params: Any,
        manifest: dict = None,
        request_id: str = None,
    ):
        request_id = request_id
        tickers_tuple = tuple(sorted(params.tickers)) 
        ai_analysis = params.ai_analysis
        df = self.market_data_repo.fetch_data(
            tickers=tickers_tuple,
            start_date=params.start_date,
            end_date=params.end_date,
        ) 

        if df is None:
            return {"error": "Um ou mais tickers são inválidos."}

        if df.empty:
            return {"error": "Dados insuficientes para o intervalo selecionado."}

        close_prices = df["Close"]
        if settings.CACHE:
            if not os.path.exists(settings.ASSET_CACHE_DIR):
                os.makedirs(settings.ASSET_CACHE_DIR)
            close_prices.to_parquet(f"{settings.ASSET_CACHE_DIR}/{request_id}.{settings.EXT_CACHE}", compression=settings.COMPRESSION)

        returns_data = ReturnEngine().calculate(close_prices)
        returns = returns_data["returns"]

        correlation_data = CorrelationEngine().calculate(returns)

        individual = IndividualMetricsEngine().calculate(
            returns, settings.RISK_FREE_RATE
        )

        portfolio = PortfolioMetricsEngine().calculate(
            returns, settings.RISK_FREE_RATE
        )

        payload ={
            "results": {
            "portfolio": portfolio,
            "correlation_matrix": correlation_data,
            "individual_metrics": individual
            }
        }
        use_case = AnalyzeTextUseCase()
        payload_string = json.dumps(
            jsonable_encoder(payload),
            ensure_ascii=False
        )

        ai_analysis = None if not ai_analysis else use_case.execute(FinanceiroPromptContract(), payload_string)
        # --- format to genai prompt ---

        result = PortfolioMetricsResponseAssembler.build(
            request_id=request_id,
            params=params,
            engine_portfolio=manifest["portfolio_engine"],
            engine_Correlation=manifest["correlation_engine"],
            engine_IndividualMetrics=manifest["individual_engine"],
            engine_Return=manifest["return_engine"],
            result=payload,
            ai_analysis=ai_analysis
        )

        return result