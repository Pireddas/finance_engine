# app\domains\portfolio\api\portfolio_route.py
 
from fastapi import  APIRouter, Request, Depends
from app.application.config import settings
from app.domains.portfolio.schemas.portfolio_schema import PortfolioRequest, PortfolioResponse
from app.domains.portfolio.services.portfolio_service import PortfolioService
from app.platform.analytics.engine.correlation_engine import CorrelationEngine
from app.platform.analytics.engine.individual_metrics_engine import IndividualMetricsEngine
from app.platform.analytics.engine.portfolio_metrics_engine import PortfolioMetricsEngine
from app.platform.analytics.engine.return_engine import ReturnEngine


from app.application.guards.service_guard import service_guard
from app.platform.observability.log_assembler import Log
from app.application.interfaces.dependencies import (
    get_portfolio_service,
    get_return_engine,
    get_correlation_engine,
    get_portfolio_engine,
    get_individual_engine
)
from app.application.errors.semantic_error import ApplicationError

router = APIRouter(prefix="/api/v1", tags=["Portfolio"])

@router.post("/portfolio-metrics", 
             response_model=PortfolioResponse, 
             dependencies=[Depends(service_guard("portfolio_analysis"))]
        )
async def get_portfolio_metrics(
    request: Request,
    params: PortfolioRequest,
    service: PortfolioService = Depends(get_portfolio_service),
    return_engine: ReturnEngine = Depends(get_return_engine),
    correlation_engine: CorrelationEngine = Depends(get_correlation_engine),
    portfolio_engine: PortfolioMetricsEngine = Depends(get_portfolio_engine),
    individual_engine: IndividualMetricsEngine = Depends(get_individual_engine),
):
    
    request.state.payload = params.model_dump()

    request_id=getattr(request.state, "request_id", "unknown")

    Log(service_name="portfolio-metrics", params=params, request_id=request_id).info()

    if (params.ai_analysis) and (not settings.OPENAI_API_KEY):
        raise ApplicationError("NO_API_KEYS") 
    
    return_manifest = return_engine.metadata()
    Log(service_name="portfolio-metrics", params=return_manifest, request_id=request_id).debug()
    
    correlation_engine = correlation_engine.metadata()
    Log(service_name="portfolio-metrics", params=correlation_engine, request_id=request_id).debug()
    
    portfolio_engine = portfolio_engine.metadata()
    Log(service_name="portfolio-metrics", params=portfolio_engine, request_id=request_id).debug()
    
    individual_engine = individual_engine.metadata()
    Log(service_name="portfolio-metrics", params=individual_engine, request_id=request_id).debug()
    
    manifest = {
        "return_engine": return_manifest,
        "correlation_engine": correlation_engine,
        "portfolio_engine": portfolio_engine,
        "individual_engine": individual_engine,
    }

    result = service.get_portfolio_metrics(
        params=params,
        manifest=manifest,
        request_id=request_id
    )

    return result
