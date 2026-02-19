# app\platform\observability\log_metadata\metadata.py
 
from fastapi import params

class LogAssembler:

    @staticmethod
    def debug(service_name: str, request_id: str, params: params) -> str:
        try:
            version_str = ", ".join(
                f"{k}: {v}" for k, v in params.items()
            )
            result = f"ID: {request_id} | Version: {version_str}"

        except AttributeError as e:
            raise ValueError(f"Erro: {service_name} - {e}")
        
        return result
        
    @staticmethod
    def info(service_name: str, request_id: str, params: params) -> str:
        try:
            if service_name=="basic-metrics":
                result = (
                    f"ID: {request_id} | "
                    f"Service: {service_name} | "
                    f"ticker: {params.ticker} | "
                    f"benchmark: {params.benchmark} | "
                    f"start_date: {params.start_date} | "
                    f"end_date: {params.end_date} | "
                )
            elif service_name=="risk-metrics":
                result = (
                    f"ID: {request_id} | "
                    f"Service: {service_name} | "
                    f"ticker: {params.ticker} | "
                    f"start_date: {params.start_date} | "
                    f"end_date: {params.end_date} | "
                )
            elif service_name=="portfolio-metrics":
                result = (
                    f"ID: {request_id} | "
                    f"Service: {service_name} | "
                    f"tickers: {params.tickers} | "
                    f"start_date: {params.start_date} | "
                    f"end_date: {params.end_date} | "
                )
        except AttributeError as e:
            raise ValueError(f"Erro: {service_name} - {e}")
        
        return result