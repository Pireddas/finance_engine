# app\application\assemblers\risk_assembler.py

class RiskMetricsResponseAssembler:
<<<<<<< HEAD
 
=======

>>>>>>> c0d53267f71c88994253d019eb96ea0b0b1e7383
    @staticmethod
    def build(
        request_id: str,
        params,
        engine_manifest: dict,
<<<<<<< HEAD
        results: dict,
        ai_analysis: str
=======
        results: dict
>>>>>>> c0d53267f71c88994253d019eb96ea0b0b1e7383
    ) -> dict:
        return {
            "request_id": request_id,
            "engine_specification": {
                "engine_risk_metrics": {
                    "engine": engine_manifest["formula_version"],
                    "engine_version": engine_manifest["engine_version"],
                    "effective_date": engine_manifest["effective_date"],
                }
            },
            "symbol": params.ticker,
            "parameters": {
                "start_date": params.start_date,
                "end_date": params.end_date,
            },
            "results": results,
<<<<<<< HEAD
            "ai_analysis": ai_analysis
=======
>>>>>>> c0d53267f71c88994253d019eb96ea0b0b1e7383
        }
