# app\platform\analytics\engine\risk_metrics.py

import numpy as np
import pandas as pd
from app.platform.analytics.metadata.manifests import tail_risk_manifest

class TailRiskEngine:
    manifest = tail_risk_manifest()

    def metadata(self):
        return self.manifest

    def calculate(self, data: pd.Series):
        # Garante que temos uma Series
        if isinstance(data, pd.DataFrame):
            data = data.iloc[:, 0]
        
        # Limpeza inicial
        data = data.dropna()

        # LOGICA DE CONVERSÃO: Se os dados parecerem preços (ex: PETR4 a R$ 26,00),
        # transformamos em retornos percentuais.
        # Se a média for muito diferente de zero ou não houver valores negativos, 
        # provavelmente são preços nominais.
        if data.min() > 0 and data.mean() > 1:
            returns = data.pct_change().dropna()
        else:
            returns = data

        # Remove valores infinitos (caso ocorra divisão por zero no pct_change)
        returns = returns.replace([np.inf, -np.inf], np.nan).dropna()

        confidences = [95, 98, 99, 99.9]
        results = {}

        for conf in confidences:
            # Em retornos, o VaR é o percentil da cauda esquerda (prejuízos)
            percentile_val = 100 - conf
            var_val = np.percentile(returns, percentile_val)

            # CVaR: Média dos retornos que são menores ou iguais ao VaR
            tail_returns = returns[returns <= var_val]
            cvar_val = tail_returns.mean() if not tail_returns.empty else var_val

            key = str(conf).replace(".", "_")
            # Multiplicamos por 100 para exibir em formato percentual legível (opcional)
            # Aqui mantive o decimal (ex: -0.02) que é o padrão de cálculo
            results[f"var_{key}"] = float(var_val)
            results[f"cvar_{key}"] = float(cvar_val)

        results["worst_day"] = float(returns.min())
        results["daily_std"] = float(returns.std())

        mean_return = float(returns.mean())
        
        # O Z-Score agora faz sentido: (Pior Retorno - Média dos Retornos) / Desvio Padrão
        z_score = (
            (results["worst_day"] - mean_return) / results["daily_std"]
            if results["daily_std"] != 0
            else 0
        )

        results["z_score_worst"] = float(z_score)

        return results
    
    def short_calculate(self, data: pd.Series):
            # Garante que temos uma Series
            if isinstance(data, pd.DataFrame):
                data = data.iloc[:, 0]
            
            # Limpeza inicial
            data = data.dropna()

            # Converte preços em retornos percentuais se necessário
            if data.min() > 0 and data.mean() > 1:
                returns = data.pct_change().dropna()
            else:
                returns = data

            returns = returns.replace([np.inf, -np.inf], np.nan).dropna()

            # Para o Short, as confianças são os percentis altos (ex: 95, 99)
            confidences = [95, 98, 99, 99.9]
            results = {}

            for conf in confidences:
                # VaR para Short: usamos o percentil diretamente (ex: os 5% maiores retornos)
                # Se conf=95, buscamos o valor que 95% dos retornos estão ABAIXO dele.
                var_val = np.percentile(returns, conf)

                # CVaR para Short: Média dos retornos que são MAIORES ou iguais ao VaR
                # Representa a média das "explosões" de alta acima do limite do VaR
                tail_returns = returns[returns >= var_val]
                cvar_val = tail_returns.mean() if not tail_returns.empty else var_val

                key = str(conf).replace(".", "_")
                results[f"var_{key}"] = float(var_val)
                results[f"cvar_{key}"] = float(cvar_val)

            # O "pior dia" para o vendido é a MAIOR alta registrada
            results["worst_day"] = float(returns.max())
            results["daily_std"] = float(returns.std())

            mean_return = float(returns.mean())
            
            # O Z-Score medindo quão longe a maior alta foi da média
            z_score = (
                (results["worst_day"] - mean_return) / results["daily_std"]
                if results["daily_std"] != 0
                else 0
            )

            results["z_score_worst"] = float(z_score)

            return results