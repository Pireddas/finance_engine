# app\application\assemblers\portfolio_assembler.py
from app.platform.analytics.metadata.manifests import (
    return_portfolio_manifest,
    individual_portfolio_manifest,
    correlation_portfolio_manifest,
    portifolio_manifest
)


class PortfolioMetricsResponseAssembler:

    @staticmethod
    def build(
        request_id: str,
        params,
        engine_portfolio: dict,
        engine_Correlation: dict,
        engine_IndividualMetrics: dict,
        engine_Return: dict,
        result: dict,
        ai_analysis: str
    ) -> dict:
        return {
            "request_id": request_id,
            "engine_specification": {
                    "engine_metrics": {
                        "engine": engine_portfolio["formula_version"],
                        "effective_date": engine_portfolio["effective_date"],
                        "manifest": portifolio_manifest()
                    },
                    "engine_return": {
                        "engine": engine_Return["formula_version"],
                        "effective_date": engine_Return["effective_date"],
                        "manifest": return_portfolio_manifest()
                        
                    },
                    "engine_individual_metrics": {
                        "engine": engine_IndividualMetrics["formula_version"],
                        "effective_date": engine_IndividualMetrics["effective_date"],
                        "manifest": individual_portfolio_manifest()
                    },
                    "engine_correlation": {
                        "engine": engine_Correlation["formula_version"],
                        "effective_date": engine_Correlation["effective_date"],
                        "manifest": correlation_portfolio_manifest()
                    }
                },
            "tickers": params.tickers,
            "parameters": {
                "start_date": params.start_date,
                "end_date": params.end_date
            },
            "results": result["results"],
            "ai_analysis": ai_analysis
        }
