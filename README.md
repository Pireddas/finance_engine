# Financial Metrics API (v0.1.0)


[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green)](#) 

## Disclaimer

Esse projeto é um estudo de caso fictício, baseados em situações reais vivenciadas no ambiente corporativo. Tem como objetivo apresentar um modelo concreto e estruturado, sem expectativas de alcançar a perfeição de forma isolada.

Uma entrega com excelência é construída através do trabalho em equipe, ouvindo o contraditório e encontrando pontos de equilíbrio. 

## 📌 Visão Geral

A **Financial Metrics API** é uma solução de análise quantitativa avançada voltada para a gestão de ativos e risco financeiro. Diferente de scripts financeiros simples, este projeto foi construído sob princípios de **Domain-Driven Design (DDD)** e **Arquitetura Limpa**, focando em três pilares:

1.  **Precisão Quantitativa:** Métricas de performance, risco de cauda (Tail Risk) e análise de portfólio.
2.  **Governança:** Controle de acesso via API Keys com persistência segura, rastreabilidade e auditoria de uso.
3.  **Observabilidade:** Rastreabilidade total de requisições, logs estruturados e monitoramento de performance.

---

## 🏗️ Arquitetura e Design

O projeto utiliza uma divisão por **Domínios**, isolando a lógica de negócio das implementações técnicas e provedores externos.

### Estrutura de Camadas
* **Domains (`app/domains`):** Cada domínio (Finance, Risk, Portfolio, Auth) possui seus próprios serviços, esquemas (Pydantic) e definições de interface.
* **Infrastructure (`app/infrastructure`):** Implementações concretas de acesso a dados (integração com Yahoo Finance via `yfinance`) e persistência (SQLite para gestão de chaves).
* **Application (`app/application`):** Configurações globais via Pydantic Settings, bootstrapping do banco de dados e o container de dependências.
* **Platform (`app/platform`):** Recursos transversais (cross-cutting concerns) como middlewares de segurança, auditoria e utilitários de gestão.

---

## 🧾 Engine Versioning & Methodology Governance (Design Principle)

Embora este projeto esteja focado no desenvolvimento dos motores quantitativos, sua arquitetura já foi concebida considerando a futura implementação de um **Framework de Governança de Regras, Parâmetros e Metodologias**.

Cada resposta da API não retorna apenas resultados numéricos.  
Ela inclui explicitamente um bloco `engine_specification`, contendo:

- Identificação da metodologia aplicada  
- Versão da engine  
- Data de vigência (`effective_date`)  
- Premissas estatísticas e parâmetros estruturais  
- Manifesto técnico completo da fórmula utilizada  

Exemplo simplificado de retorno:

```json
{
  "engine_specification": {
    "engine_risk_metrics": {
      "effective_date": "2024-08-15",
      "manifest": {
        "engine": "tail_risk",
        "engine_version": "1.2.0",
        "formula_version": "historical_var_cvar",
        "dataframe_version": "close_prices_adjusted",
        "assumptions": "iid_returns",
        "created_at": "2024-08-11",
        "effective_date": "2024-08-15"
      }
    }
  }
}
```
Em sistemas convencionais, regras de cálculo permanecem ocultas no código-fonte.  
Nesta arquitetura, metodologias são tratadas como **ativos institucionais explícitos**, com versionamento e rastreabilidade formal.

Atualmente, os manifests são definidos por funções estáticas, representando uma simulação controlada de governança. Essa decisão é intencional: o projeto já está preparado para que, futuramente, essas definições sejam:

- Armazenadas em banco de dados  
- Submetidas a workflow de aprovação  
- Vinculadas a alçadas institucionais  
- Controladas por máquina de estados (*Draft → Challenger → Champion → Deprecated*)  

---

### 🧠 Princípio Arquitetural

O motor devolve resultados brutos e auditáveis.  
A política metodológica é desacoplada da execução matemática.

Esse design permite que o sistema evolua para um ambiente regulatório completo — incluindo estratégias *Champion-Challenger*, auditoria histórica e reconstituição de cálculos — sem necessidade de refatorações estruturais profundas.

---

### 📌 Benefícios Estruturais

- Versionamento explícito de metodologia  
- Rastreabilidade por `request_id`  
- Preservação de contratos externos  
- Preparação para compliance regulatório  
- Evolução controlada de modelos quantitativos  

O projeto, portanto, não é apenas uma API de métricas financeiras, mas a fundação de um motor analítico institucional preparado para governança formal.

---

### 🔗 Integração com Framework de Governança (Projeto 5)

A estrutura de `engine_specification` foi desenhada para integração direta com o projeto:

**5 – Framework de Governança de Regras, Parâmetros e Metodologias**

Neste framework, regras e parâmetros deixam de ser definidos estaticamente e passam a ser tratados como ativos versionados em banco de dados, submetidos a fluxo formal de validação e aprovação institucional.

O modelo prevê:

- Gestão de ciclo de vida (Draft → Challenger → Champion → Deprecated)
- Estratégias Champion-Challenger e A/B Testing metodológico
- Registro de alçadas de aprovação
- Auditoria histórica completa de transições de versão
- Reconstituição exata de cálculos passados

O motor atual já respeita essa futura arquitetura ao:

- Separar cálculo de política metodológica
- Expor metadados estruturados por engine
- Manter rastreabilidade via `request_id`
- Preservar estabilidade contratual da API

Quando o Framework de Governança for implementado, os manifests deixarão de ser estáticos e passarão a ser resolvidos dinamicamente a partir do repositório institucional de metodologias homologadas.

---

## 🧩 Domínios do Sistema

### 🔐 Auth & Governance
Responsável pelo ciclo de vida de credenciais e segurança da API.
* **Segurança:** Middleware `SQLiteAuthMiddleware` que intercepta requisições e valida headers `X-API-KEY` usando hash SHA-256.
* **Gestão:** Scripts e serviços para criação, ativação e revogação de chaves com associação a proprietários (*owners*).

### 📊 Finance Metrics
Análise de performance e volatilidade de ativos individuais.
* **Métricas:** Retorno Total, CAGR (Taxa de Crescimento Anual Composta), Volatilidade Anualizada e Sharpe Ratio.
* **Validação:** Engine de validação de tickers para garantir a integridade dos dados históricos processados.

### ⚠️ Risk Analysis
Foco em estatísticas de eventos extremos e gestão de perdas.
* **Tail Risk:** Cálculo de **VaR (Value at Risk)** e **CVaR (Conditional VaR)** via simulação histórica.
* **Estresse:** Suporte a múltiplos níveis de confiança (95%, 98%, 99% e 99.9%).

### 📈 Portfolio Analysis
Análise de cestas de ativos e diversificação.
* **Correlação:** Geração de matriz de correlação para identificar dependências entre ativos.
* **Métricas Agregadas:** Volatilidade do portfólio e performance ponderada.

---

> Você pode acessar o terminal de teste visual em `/application_test` para validar a saída destes dados em uma interface amigável.  
> Exemplo: http://127.0.0.1:8002/application_test

---

## 🛠️ Tecnologias e Boas Práticas
* **FastAPI:** Framework moderno de alta performance com suporte a tipagem estática.
* **Pydantic:** Validação de dados e contratos de API (Schemas).
* **Pandas & NumPy:** Engine matemática para processamento de séries temporais financeiras.
* **Poetry:** Gestão de dependências e isolamento de ambiente.
* **Observabilidade:** Middleware de logs estruturados com `request_id` e métricas de tempo de execução.

---

## 🚀 Evolução da Arquitetura (Roadmap)

O projeto foi desenhado para ser extensível, com um roadmap claro para ambientes de produção em larga escala:

1.  **Injeção de Dependências Nativa:** Migrar a instanciação manual para o sistema de `Depends` do FastAPI ou um container IoC dedicado.
2.  **Concurrency (Async/Await):** Tornar as chamadas à infraestrutura (APIs de mercado) assíncronas para aumentar o throughput.
3.  **Caching Layer:** Implementar cache distribuído (Redis) para dados de mercado, minimizando latência e custos de API.
4.  **Database Migration:** Substituir a gestão manual do banco por **Alembic** para versionamento de esquema.
5.  **Persistência Configurável:** (SQLite / PostgreSQL)
    - Necessidade de suportar ambientes distintos (dev vs produção)
    - SQLite é suficiente para desenvolvimento local e testes
    - PostgreSQL é mais adequado para concorrência, volume e produção


---

## ▶️ Executando o Projeto

1.  **Instalação:**
    ```bash
    poetry install
    ```
2.  **Configuração:**
    Configure o arquivo `.env` com as definições de `RISK_FREE_RATE`, `DEFAULT_BENCHMARK`, `DB_PATH`, etc.
3.  **Execução:**
    ```bash
    poetry run python main.py
    
    # http://127.0.0.1:8000/
    ```
4.  Criar uma **API Key** utilizando a ferramenta: `app/platform/utils/manage_keys.py`
    ```bash
    python -m app.platform.utils.manage_keys
    ```

6.  **Documentação:**
    Acesse `/docs` para visualizar o Swagger UI ou `/redoc` para documentação técnica.


## Observação final
Este projeto representa um recorte técnico de uma arquitetura mais ampla que, em ambiente corporativo real, envolveria múltiplas áreas, fluxos formais de aprovação e um volume significativo de documentação institucional.

Os documentos disponíveis na pasta `/docs` são exemplos que ilustram como esse processo ocorreria em um contexto corporativo completo. Eles não representam a totalidade de artefatos formais que existiriam em um ambiente real, mas demonstram o modelo de governança e tomada de decisão que fundamenta e orienta todo o ciclo de definição, validação e entrega de soluções.


---
📌 *Designed for governance. Built for evolution.*

