# app\domains\risk\schemas\risk_schema.py

from pydantic import BaseModel, Field
from typing import Optional, Dict

# --- INPUT (Request) ---
class RiskMetricsRequest(BaseModel):
    ticker: str = Field(..., json_schema_extra={"example": "PETR4.SA"}, description="Ticker do ativo")
    short: Optional[bool] = Field(False, description="Operação short?")
    start_date: Optional[str] = Field(None, json_schema_extra={"example": "2024-01-01"}, description="Data de início (AAAA-MM-DD)")
    end_date: Optional[str] = Field(None, json_schema_extra={"example": "2024-12-31"}, description="Data de fim (AAAA-MM-DD)")
    ai_analysis: Optional[bool] = Field(False, description="Incluir análise de IA nos resultados")
    
# --- COMPONENTES (Internal Results) ---
class RiskResults(BaseModel):
    # Value at Risk (VaR)
    var_95: float = Field(..., description="VaR Histórico 95%")
    var_98: float = Field(..., description="VaR Histórico 98%")
    var_99: float = Field(..., description="VaR Histórico 99%")
    var_99_9: float = Field(..., description="VaR Histórico 99.9% (Evento de Cauda Extrema)")
    
    # Conditional VaR (CVaR / Expected Shortfall)
    cvar_95: float = Field(..., description="Expected Shortfall 95%")
    cvar_98: float = Field(..., description="Expected Shortfall 98%")
    cvar_99: float = Field(..., description="Expected Shortfall 99%")
    cvar_99_9: float = Field(..., description="Expected Shortfall 99.9%")
    
    # Estatísticas de Volatilidade e Extremos
    worst_day: float = Field(..., description="Pior retorno diário registrado no período")
    daily_std: float = Field(..., description="Desvio Padrão Diário (Volatilidade Diária)")
    z_score_worst: float = Field(..., description="Z-Score do pior dia (quão anômala foi a queda)")

class RiskMetricsEngine(BaseModel):
    effective_date: Optional[str] = Field(None, json_schema_extra={"example": "2023-12-31"}, description="Data de início da vigência (AAAA-MM-DD)")
    manifest: Dict
    
class EngineSpec(BaseModel):
    engine_risk_metrics: RiskMetricsEngine

# --- OUTPUT (Response) ---
class RiskMetricsResponse(BaseModel):
    request_id: str = Field(..., description="Hash único para auditoria da requisição")
    engine_specification: EngineSpec
    symbol: str = Field(..., description="Ticker analisado")
    parameters: dict = Field(..., description="Dicionário com as datas e período aplicados")
    results: RiskResults = Field(..., description="Métricas de risco calculadas")
    ai_analysis: Optional[str] = Field(None, description="Análise gerada por IA, se solicitada")