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
        results = self.engine.calculate(returns)

        use_case = AnalyzeTextUseCase()
        payload_string = json.dumps(results, ensure_ascii=False)
        ai_analysis = None if not ai_analysis else use_case.execute(FinanceiroPromptContract(), payload_string)
        # --- format to genai prompt ---
        
        return results, ai_analysis
        # confidences = [95, 98, 99, 99.9]
        # results_map = {}

        # # Garanta que 'returns' seja uma Series (evita erro de DataFrame)
        # if isinstance(returns, pd.DataFrame):
        #     returns = returns.iloc[:, 0]

        # for conf in confidences:
        #     # 95% confiança = 5º percentil
        #     percentile_val = 100 - conf
        #     var_val = np.percentile(returns, percentile_val)
            
        #     # Filtramos os retornos que estão na cauda (menores ou iguais ao VaR)
        #     tail_returns = returns[returns <= var_val]
            
        #     # Calculamos o CVaR: se a cauda não estiver vazia, média. Caso contrário, o próprio VaR.
        #     if not tail_returns.empty:
        #         cvar_val = tail_returns.mean()
        #     else:
        #         cvar_val = var_val
            
        #     # Formatação das chaves para o Schema (ex: var_99_9)
        #     key_suffix = str(conf).replace('.', '_')
        #     results_map[f"var_{key_suffix}"] = round(float(var_val), 4)
        #     results_map[f"cvar_{key_suffix}"] = round(float(cvar_val), 4)

        # # Métricas fixas
        # results_map["worst_day"] = round(float(returns.min()), 4)
        # results_map["daily_std"] = round(float(returns.std()), 4)

        # # Média dos retornos para o cálculo do Z-Score
        # mean_return = float(returns.mean())
        # z_score = (results_map["worst_day"] - mean_return) / results_map["daily_std"]
        # results_map["z_score_worst"] = round(float(z_score), 2)

        # return results_map
