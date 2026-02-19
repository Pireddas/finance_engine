# app/application/dependencies.py

from fastapi import Depends

from app.infrastructure.market_data.yfinance_repository import (
    YFinanceBasicRepository, 
    YFinanceRiskRepository,
    YFinancePortfolioRepository
)

from app.domains.finance.repositories.market_data import BasicRepository
from app.domains.finance.services.basic_metrics_service import BasicMetricsService
from app.platform.analytics.engine.basic_metrics import BasicMetricsEngine

from app.domains.risk.repositories.market_data import RiskRepository
from app.domains.risk.services.risk_metrics_service import RiskMetricsService
from app.platform.analytics.engine.risk_metrics import TailRiskEngine

from app.domains.portfolio.repositories.market_data import PortfolioRepository
from app.domains.portfolio.services.portfolio_service import PortfolioService
from app.platform.analytics.engine.correlation_engine import CorrelationEngine
from app.platform.analytics.engine.individual_metrics_engine import IndividualMetricsEngine
from app.platform.analytics.engine.return_engine import ReturnEngine
from app.platform.analytics.engine.portfolio_metrics_engine import PortfolioMetricsEngine

def get_portfolio_repo() -> PortfolioRepository:
    return YFinancePortfolioRepository()

def get_portfolio_service(
    repo: PortfolioRepository = Depends(get_portfolio_repo),
) -> PortfolioService:
    return PortfolioService(market_data_repo=repo)

def get_portfolio_engine() -> PortfolioMetricsEngine:
    return PortfolioMetricsEngine()
def get_correlation_engine() -> CorrelationEngine:
    return CorrelationEngine()
def get_individual_engine() -> IndividualMetricsEngine:
    return IndividualMetricsEngine()
def get_return_engine() -> ReturnEngine:
    return ReturnEngine()


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
