# app\application\assemblers\risk_assembler.py
from app.platform.analytics.metadata.manifests import tail_risk_manifest

class RiskMetricsResponseAssembler:
 
    @staticmethod
    def build(
        request_id: str,
        params,
        engine_manifest: dict,
        results: dict,
        ai_analysis: str
    ) -> dict:
        return {
            "request_id": request_id,
            "engine_specification": {
                "engine_risk_metrics": {
                    "effective_date": engine_manifest["effective_date"],
                    "manifest": tail_risk_manifest()
                }
            },
            "symbol": params.ticker,
            "parameters": {
                "start_date": params.start_date,
                "end_date": params.end_date,
            },
            "results": results,
            "ai_analysis": ai_analysis
        }
