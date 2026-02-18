# app/application/dependencies.py

from fastapi import Depends
from app.domains.finance.repositories.market_data import BasicRepository
from app.infrastructure.market_data.yfinance_repository import YFinanceBasicRepository, YFinanceRiskRepository
from app.domains.finance.services.basic_metrics_service import BasicMetricsService
from app.platform.analytics.engine.basic_metrics import BasicMetricsEngine
from app.domains.risk.repositories.market_data import RiskRepository
from app.domains.risk.services.risk_metrics_service import RiskMetricsService
from app.platform.analytics.engine.risk_metrics import TailRiskEngine

def get_market_repo() -> BasicRepository:
    return YFinanceBasicRepository()

def get_metrics_service(
    repo: BasicRepository = Depends(get_market_repo),
) -> BasicMetricsService:
    return BasicMetricsService(market_data_repo=repo)

def get_engine() -> BasicMetricsEngine:
    return BasicMetricsEngine()


def get_risk_repo() -> RiskRepository:
    return YFinanceRiskRepository()

def get_risk_service(
    repo: RiskRepository = Depends(get_risk_repo),
) -> RiskMetricsService:
    return RiskMetricsService(market_data_repo=repo)

def get_risk_engine() -> TailRiskEngine:
    return TailRiskEngine()
