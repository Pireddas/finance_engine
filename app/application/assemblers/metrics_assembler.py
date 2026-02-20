# app/application/assemblers/metrics_assembler.py
from app.platform.analytics.metadata.manifests import basic_metrics_manifest
class MetricsResponseAssembler:

    @staticmethod
    def build(
        request_id: str,
        engine_manifest: dict,
        result: dict,
        ai_analysis: str
    ) -> dict:
        
        result["request_id"] = request_id
        result["engine_specification"] = {
            "engine_metrics": {
                "engine": engine_manifest["formula_version"],
                "effective_date": engine_manifest["effective_date"],
                "manifest": basic_metrics_manifest()
            }
        }
        result["ai_analysis"] = ai_analysis
        return result
