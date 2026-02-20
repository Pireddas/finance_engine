# app\domains\risk\api\risk_route.py

from fastapi import APIRouter, Request, Depends
from app.application.config import settings
from app.domains.risk.schemas.risk_schema import RiskMetricsRequest, RiskMetricsResponse
from app.domains.risk.services.risk_metrics_service import RiskMetricsService
from app.application.guards.service_guard import service_guard
from app.platform.analytics.engine.risk_metrics import TailRiskEngine
from app.application.assemblers.risk_assembler import RiskMetricsResponseAssembler
from app.application.interfaces.dependencies import get_risk_service, get_risk_engine
from app.platform.observability.log_assembler import Log
from app.application.errors.semantic_error import ApplicationError

router = APIRouter(prefix="/api/v1", tags=["Risk"])
 
# Alterado para POST 
@router.post("/risk-metrics", response_model=RiskMetricsResponse, dependencies=[Depends(service_guard("basic_metrics"))])
async def get_risk_metrics(
    request: Request, 
    params: RiskMetricsRequest,
    service: RiskMetricsService = Depends(get_risk_service)
    ):

    request.state.payload = params.model_dump()
    request_id = getattr(request.state, "request_id", "unknown")

    Log(service_name="risk-metrics", params=params, request_id=request_id).info()

    if (params.ai_analysis) and (not settings.OPENAI_API_KEY):
        raise ApplicationError("NO_API_KEY") 
    
    result = service.get_risk_metrics(
        params=params,
        **params.model_dump(), 
        request_id=request_id,
        )
    
    Log(service_name="risk-metrics", params=result["engine_specification"], request_id=request_id).debug()

    return result
