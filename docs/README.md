# projeto_corporativo

#

# Matriz de Fases x Envolvidos — Projeto Corporativo

| Fase | Objetivo | Documentos / Artefatos | Envolvidos Principais | Natureza da Atividade |
|------|----------|-----------------------|---------------------|---------------------|
| 1. Conversas Informais | Explorar melhorias ou oportunidades | Nenhum formal | Produto, Diretoria | Discussão exploratória, brainstorming |
| 2. Registro de Oportunidade / Problema | Formalizar demanda | `business_problem.md` | Produto, Diretoria, PMO | Registro inicial do problema, definição de escopo preliminar |
| 3. Definição de Requisitos | Transformar problema em requisitos de negócio | `business_requirements.md` | PMO, Produto, Diretoria, Arquitetura | Planejamento estratégico, alinhamento institucional, validação de requisitos |
| 4. Planejamento Estratégico | Planejar fases evolutivas e resumir visão executiva | `evolutionary_phases.md`, `one_pager_executive.md` | PMO, Arquitetura, Produto, Diretoria | Definição de roadmap, priorização, visão consolidada |
| 5. Transição para Execução | Preparar documentação técnica e operacional | `functional_specification.md`, `user_stories.md`, ADRs, planos de teste | PMO, Arquitetura, Desenvolvimento, QA | Tradução de estratégia em especificações, casos de uso e critérios de aceitação |
| 6. Desenvolvimento e Implementação | Implementar, testar e validar solução | Código em `src/`, testes unitários, ADRs locais, documentação técnica de serviço | Desenvolvimento, QA, Operações | Execução concreta do projeto seguindo protocolos e padrões institucionais |
| 7. Entrega e Auditoria | Garantir rastreabilidade e conformidade | Relatórios padronizados, logs, auditoria | Produto, Arquitetura, QA, Diretoria | Validação final, auditoria e registro histórico |

---
---

**Container Organizacional do Projeto**

> Este diretório não é um repositório, nem contém código executável.  
> Ele serve apenas para **agregar e organizar os repositórios relacionados** a este projeto corporativo, garantindo clareza institucional, rastreabilidade e consistência de arquitetura.

---

## Estrutura de Diretórios

```text
projeto_corporativo/
 ├─ framework_back_end/              <- Repositório Back-End (src/ = raiz)
 ├─ framework_cliente/               <- Repositório Cliente / Front-Protocolo (src/ = raiz)
 └─ framework_calculo_de_metricas/   <- Repositório do Serviço de Cálculo (src/ = raiz)
```

# Arquitetura Corporativa — Visão de Repositórios e Protocolos

## Repositórios

### 1. framework_back_end
**Repositório soberano do backend**

- `src/` é a raiz do código
- Responsabilidades:
  - Orquestração do fluxo de execução
  - Validação de identidade e contratos
  - Integração com serviços internos (ex.: cálculo)
  - Registro de logs e auditoria
- Restrições:
  - Não conhece clientes diretamente
  - Comunicação ocorre exclusivamente via **Execution Protocol**

---

### 2. framework_cliente
**Repositório soberano do cliente (CLI ou Web)**

- `src/` é a raiz do código
- Responsabilidades:
  - Serialização e envio da Execution Identity
  - Interface CLI e Web para envio de parâmetros
  - Recepção de resultados e exibição
  - Modelos compartilhados do protocolo
- Restrições:
  - Não conhece lógica interna do backend
  - Depende apenas do contrato do protocolo

---

### 3. framework_calculo_de_metricas
**Repositório independente de processamento financeiro**

- `src/` é a raiz do código
- Responsabilidades:
  - Implementação de métricas financeiras (CAGR, Sharpe, Volatilidade etc.)
  - Lógica de cálculo puro
  - Retorno de resultados ao backend
- Restrições:
  - Não conhece clientes
  - Recebe apenas dados estruturados do backend

---

## Princípios Arquiteturais

- Separação clara de responsabilidades
- Cada repositório é soberano e autônomo
- Backend orquestra, cliente consome, cálculo processa
- Evolução independente de código e ciclo de vida

---

## Execution Protocol

- Contrato formal entre **cliente** e **backend**
- Garante:
  - Rastreabilidade
  - Reprodutibilidade
  - Auditoria
- Transporte independente de canal:
  - CLI
  - Web
  - Clientes futuros

---

## Convenção de Raiz (`src/`)

- Cada repositório define `src/` como raiz do código
- Imports:
  - Absolutos
  - Previsíveis
- Tudo acima de `src/`:
  - Documentação
  - Testes
  - CI/CD
  - Infraestrutura

---

## Extensibilidade

- Novos serviços podem ser adicionados no mesmo nível
- Novos clientes podem consumir o backend sem alterar o core
- Nenhum impacto cruzado não planejado

---

## Fluxo de Execução Conceitual

```text
Cliente (framework_cliente)
        │
        ▼
Backend (framework_back_end)
        │
        ▼
Serviço de Cálculo (framework_calculo_de_metricas)
        │
        ▼
Backend agrega resultados
        │
        ▼
Cliente recebe e exibe
```
## 7. Diagrama Visual do Fluxo de Execução

```mermaid
flowchart TD
    subgraph Cliente [Cliente (framework_cliente)]
        direction TB
        CLI[CLI / Web]
        srcC[src/]
    end

    subgraph Backend [Backend (framework_back_end)]
        direction TB
        srcB[src/]
    end

    subgraph Calculo [Serviço de Cálculo (framework_calculo_de_metricas)]
        direction TB
        srcCalc[src/]
    end

    %% Fluxo de chamadas
    CLI -->|Chamada via Protocolo| srcB
    srcB -->|Solicitação de Cálculo| srcCalc
    srcCalc -->|Retorno de Métricas| srcB
    srcB -->|Resposta ao Cliente| CLI

    %% Execution Identity
    CLI -.->|Execution Identity| srcCalc
```
___
___

# framework_back_end

## 1. Estrutura do Repositório

```text
framework_back_end/
├─ docs/                                    <- Documentação do backend
├─ tests/                                   <- Testes unitários e de integração
├─ ci/                                      <- Scripts de CI/CD
├─ scripts/                                 <- Scripts utilitários (migração, setup)
├─ pyproject.toml                           <- Configuração do Poetry
└─ src/                                     <- Raiz do código do backend
    ├─ bootstrap.py                         <- Ponto de entrada principal
    ├─ execution_protocol/                  <- Protocolo de comunicação e Execution Identity
    ├─ application/                         <- Casos de uso e orquestração
    ├─ domain/                              <- Entidades e regras de negócio
    ├─ infrastructure/                      <- Conexões, logging e persistência
    │   ├─ connectors/                      <- Conexões externas (ex.: Custódia, APIs)
    │   ├─ persistence/                     <- DB, ORM, arquivos
    │   │   ├─ repository.py
    │   │   └─ data_loader.py
    │   ├─ logging/                         <- Logs e auditoria
    │   └─ security/                        <- Identidade, autenticação, autorização
    │       ├─ auth_service.py
    │       └─ identity_manager.py
    └─ governance/                          <- Configurações, constantes e padrões
```


## 2. src/ como Raiz do Código

Todos os imports devem ser absolutos a partir de src/

É proibido código executável fora de src/

Estrutura compatível com padrões corporativos, CI/CD e auditoria

Exemplo de import correto (em tests/):


```
from execution_protocol.identity_context import ExecutionIdentity
from application.services.orchestrator import Orchestrator
```

## 3. Configuração do Poetry

No pyproject.toml, declarar explicitamente os pacotes localizados em src/:


```
[tool.poetry]
name = "framework-back-end"
version = "0.1.0"
description = "Backend do projeto corporativo"
authors = ["Equipe Arquitetura <arquitetura@empresa.com>"]

packages = [
    { include = "execution_protocol", from = "src" },
    { include = "application", from = "src" },
    { include = "domain", from = "src" },
    { include = "infrastructure", from = "src" }
]
```


## 4. Configuração de Testes

Diretório tests/ separado de src/

Imports sempre absolutos a partir de src/

Opção A — pytest.ini



```
[pytest]
minversion = 6.0
testpaths = tests
pythonpath = src
```

Opção B — pyproject.toml

```
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
```

Comandos para execução de testes

```
poetry install
poetry shell
pytest tests/
```

## 5. Boas Práticas

Separação clara

- src/ → código de produção
- tests/ → código de teste

Execution Protocol

- Toda execução passa obrigatoriamente por execution_protocol/

Imports absolutos

- Evitam ambiguidades e falhas em CI/CD

- Código limpo

Documentação

- scripts e infraestrutura fora de src/

Ciclo de vida independente

- Soberania do backend
- Versionado via Poetry
- Independente de clientes e serviços de cálculo

## 6. Observações Institucionais

Documento serve como referência oficial para novos desenvolvedores

Alterações em:

- estrutura de pastas
- raiz do projeto
- política de imports  
  
Exigem aprovação do time de Arquitetura.

Mantém alinhamento total com:

- ramework_cliente
- framework_calculo_de_metricas

Que seguem o mesmo padrão src/ como raiz.


___
___

# framework_front_end

## 1. Estrutura do Repositório


```
framework_cliente/
├─ docs/                   <- Documentação do cliente
├─ tests/                  <- Testes unitários e de integração
├─ ci/                     <- Scripts de CI/CD (GitHub Actions, GitLab CI)
├─ scripts/                <- Scripts utilitários (setup, helpers)
├─ pyproject.toml          <- Configuração do Poetry
└─ src/                    <- Raiz do código do cliente
    ├─ bootstrap.py        <- Ponto de entrada do cliente (CLI ou Web)
    ├─ protocol/           <- Lógica do Execution Protocol
    │   ├─ protocol_definition.py
    │   ├─ serializer.py           <- Serializa Execution Identity
    │   ├─ validator.py            <- Valida parâmetros do usuário
    │   └─ dispatcher.py           <- Envia requests para backend
    │
    ├─ cli/                <- Componentes específicos da CLI
    │   ├─ commands/
    │   ├─ input_parser.py
    │   └─ output_formatter.py
    │
    ├─ web/                <- Componentes específicos da Web (API / Front)
    │   ├─ api_client.py
    │   ├─ endpoints/
    │   └─ templates/
    │
    ├─ application/        <- Casos de uso, lógica de orquestração local
    ├─ domain/             <- Entidades, value objects relacionados a cliente
    └─ governance/         <- Constantes, enums e padrões institucionais
```

## 2. src/ como Raiz do Código

- Todos os imports devem ser absolutos a partir de src/
- É proibido código executável fora de src/
- Mantém compatibilidade com padrões corporativos, CI/CD e auditoria

Exemplo de import correto (em tests/):

```
from protocol.serializer import ExecutionIdentitySerializer
from cli.input_parser import InputParser
```

---

## 3. Configuração do Poetry

No `pyproject.toml`, declarar explicitamente os pacotes localizados em `src/`:

```toml
[tool.poetry]
name = "framework-cliente"
version = "0.1.0"
description = "Cliente / Protocolo do projeto corporativo"
authors = ["Equipe Arquitetura <arquitetura@empresa.com>"]

packages = [
    { include = "protocol", from = "src" },
    { include = "cli", from = "src" },
    { include = "web", from = "src" },
    { include = "application", from = "src" },
    { include = "domain", from = "src" }
]
```
---

## 4. Configuração de Testes

- Diretório `tests/` separado de `src/`  
- Imports sempre absolutos a partir de `src/`  

Opção A — `pytest.ini`:

```ini
[pytest]
minversion = 6.0
testpaths = tests
pythonpath = src
```
Opção B — `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
```
Comandos para execução de testes:

```bash
poetry install
poetry shell
pytest tests/
```
---

## 5. Boas Práticas

- Separação clara  
  - `src/` → código de produção  
  - `tests/` → código de teste  

- **Execution Protocol**  
  - Toda execução passa obrigatoriamente por `protocol/`  
- Imports absolutos  
  - Evitam ambiguidades e falhas em CI/CD  

- **Código limpo**  
  - Scripts, templates e infraestrutura fora de `src/`  

- **Ciclo de vida independente**  
  - Cliente é soberano, versionado via Poetry, independente de backend e serviços de cálculo  

---

## 6. Observações Institucionais

- Este documento serve como referência oficial para novos desenvolvedores  

- Alterações em:  
   - Estrutura de pastas  
   - Raiz do projeto  
   - Política de imports  

- Exigem aprovação do time de Arquitetura  

- Mantém alinhamento total com:  
  - `framework_back_end`  
  - `framework_calculo_de_metricas`  

- Ambos seguem o mesmo padrão: `src/` como raiz 

___

## 8. Papéis e Responsabilidades
|Papel|	Responsabilidade|
|-|-|
|Gestor / PO	|Define regras, prioridades e aprova entregas|
|Arquiteto / Engenheiro	|Define padrões, modularidade, Execution Protocol e raiz de código|
|Dev Backend	|Implementa backend, integra serviços e persistence|
|Dev Cliente	|Implementa CLI/Web, dispatcher e serialização de Execution Identity|
|Dev Serviço de Cálculo	|Implementa métricas financeiras e retorna resultados estruturados|
|Especialista de Requisitos / QA	|Valida conformidade com MVP, regras e rastreabilidade|
|Analista CI/CD / DevOps	|Configura pipelines de teste, execução e venv/Poetry|
|Documentação / PMO	|Mantém README, diagramas Mermaid, fluxos e governança|

---

## 9. Próximos Passos

1. Definir regras funcionais e critérios de execução para backend e cliente
2. Detalhar Execution Protocol (serialização, validação, dispatcher)
3. Configurar CI/CD e testes automatizados em cada repositório
4. Documentar arquitetura e fluxos no README de cada repositório
5. Garantir rastreabilidade e reprodutibilidade completas