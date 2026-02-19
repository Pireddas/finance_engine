# app\domains\portfolio\schemas\portfolio_schema.py

from pydantic import BaseModel, Field
from typing import List, Optional, Dict

# 1. Parâmetros da Requisição (usado na Resposta)
class RequestParameters(BaseModel):
    start_date: Optional[str] = Field(None, json_schema_extra={"example": "2023-01-01"}, description="Data de início (AAAA-MM-DD)")
    end_date: Optional[str] = Field(None, json_schema_extra={"example": "2023-12-31"}, description="Data de fim (AAAA-MM-DD)")
    

# 2. Schema de ENTRADA (O que faltou no anterior)
class PortfolioRequest(BaseModel):
    tickers: List[str] = Field(..., example=["PETR4.SA", "VALE3.SA"])
    start_date: Optional[str] = Field(None, json_schema_extra={"example": "2023-01-01"}, description="Data de início (AAAA-MM-DD)")
    end_date: Optional[str] = Field(None, json_schema_extra={"example": "2023-12-31"}, description="Data de fim (AAAA-MM-DD)")
    ai_analysis: Optional[bool] = Field(False, description="Incluir análise de IA nos resultados")
    
# 3. Sub-objetos da Resposta
class PortfolioDetails(BaseModel):
    volatility: float
    sharpe: float
    expected_return: float
    cagr: float

class IndividualMetrics(BaseModel):
    cagr: Dict[str, float]
    sharpe: Dict[str, float]
    max_drawdown: Dict[str, float]
    volatility: Dict[str, float]

# 4. Agrupador de Resultados
class PortfolioResults(BaseModel):
    portfolio: PortfolioDetails
    correlation_matrix: Dict[str, Dict[str, float]]
    individual_metrics: IndividualMetrics

class Specmetrics(BaseModel):
    engine: str = Field(..., description="Versão do motor de cálculo")
    engine_version: str = Field(..., description="Versão do motor de cálculo de métricas básicas")
    effective_date: Optional[str] = Field(None, json_schema_extra={"example": "2023-12-31"}, description="Data de início da vigência (AAAA-MM-DD)")
 
class Specreturn(BaseModel):
    engine: str = Field(..., description="Versão do motor de cálculo")
    engine_version: str = Field(..., description="Versão do motor de cálculo de retorno")
    effective_date: Optional[str] = Field(None, json_schema_extra={"example": "2023-12-31"}, description="Data de início da vigência (AAAA-MM-DD)")

class Specindividual(BaseModel):
    engine: str = Field(..., description="Versão do motor de cálculo")
    engine_version: str = Field(..., description="Versão do motor de cálculo de métricas básicas individuais")
    effective_date: Optional[str] = Field(None, json_schema_extra={"example": "2023-12-31"}, description="Data de início da vigência (AAAA-MM-DD)")
 
class Speccorrelation(BaseModel):
    engine: str = Field(..., description="Versão do motor de cálculo")
    engine_version: str = Field(..., description="Versão do motor de cálculo de correlação")
    effective_date: Optional[str] = Field(None, json_schema_extra={"example": "2023-12-31"}, description="Data de início da vigência (AAAA-MM-DD)")

class EngineSpec(BaseModel):
    engine_metrics: Specmetrics
    engine_return: Specreturn
    engine_individual_metrics: Specindividual
    engine_correlation: Speccorrelation

# 5. Schema de SAÍDA Final
class PortfolioResponse(BaseModel):
    request_id: str
    engine_specification: EngineSpec
    tickers: List[str]
    parameters: RequestParameters
    results: PortfolioResults
    ai_analysis: Optional[str] = Field(None, description="Análise gerada por IA, se solicitada")