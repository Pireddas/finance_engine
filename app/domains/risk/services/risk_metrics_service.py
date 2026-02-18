# app\domains\risk\services\risk_metrics_service.py
 
import json
from app.application.config import settings
from app.platform.analytics.engine.risk_metrics import TailRiskEngine
from app.application.gpt.analyze_text import AnalyzeTextUseCase
from app.domains.risk.contract.prompt_contract import FinanceiroPromptContract

class RiskMetricsService:
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
        ticker: str,
        start_date=None,
        end_date=None,
    ):
        return self.market_data_repo.fetch_data(
            tickers=ticker,
            start_date=start_date,
            end_date=end_date
        )

    
    def get_risk_metrics(
        self, 
        ticker: str, 
        short: bool,
        start_date: str = None, 
        end_date: str = None,
        ai_analysis: bool = False,
    ):

        returns = self.market_data_repo.fetch_data(
            ticker=ticker,
            start_date=start_date,
            end_date=end_date,
        )

        if returns is None:
            return {"error": "Um ou mais tickers são inválidos."}

        if returns.empty:
            return {"error": "Dados insuficientes para o intervalo selecionado."}
        
        # --- CÁLCULOS ESTATÍSTICOS (RISCO DE CAUDA) ---

        self.engine = TailRiskEngine()
        if short != True:
            results = self.engine.calculate(returns)
        else:
            results = self.engine.short_calculate(returns)

        use_case = AnalyzeTextUseCase()
        payload_string = json.dumps(results, ensure_ascii=False)
        ai_analysis = None if not ai_analysis else use_case.execute(FinanceiroPromptContract(), payload_string)
        # --- format to genai prompt ---
        
        return results, ai_analysis

