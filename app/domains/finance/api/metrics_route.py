# app\domains\finance\api\metrics_route.py
 
from fastapi import APIRouter, Request, Depends
from app.application.config import settings
from app.domains.finance.schemas.metrics_schema import BasicMetricsRequest, BasicMetricsResponse
from app.domains.finance.services.basic_metrics_service import BasicMetricsService
from app.application.guards.service_guard import service_guard
from app.platform.observability.log_assembler import Log
from app.application.interfaces.dependencies import get_metrics_service
from app.application.errors.semantic_error import ApplicationError

router = APIRouter(prefix="/api/v1", tags=["Finance"])

@router.post("/basic-metrics", response_model=BasicMetricsResponse, dependencies=[Depends(service_guard("basic_metrics"))])
async def get_basic_metrics(
    request: Request,
    params: BasicMetricsRequest,
    service: BasicMetricsService = Depends(get_metrics_service),
):
    
    request.state.payload = params.model_dump()
    request_id = getattr(request.state, "request_id", "unknown")

    Log(service_name="basic-metrics", params=params, request_id=request_id).info()

    if (params.ai_analysis) and (not settings.OPENAI_API_KEY):
        raise ApplicationError("NO_API_KEYS") 
    
    result = service.get_metrics(
        **params.model_dump(), 
        request_id=request_id
        )

    Log(service_name="basic-metrics", params=result["engine_specification"], request_id=request_id).debug()
 
    return result
