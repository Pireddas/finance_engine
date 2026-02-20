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
___

## 4. Papéis e Responsabilidades
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

## 5. Próximos Passos

1. Definir regras funcionais e critérios de execução para backend e cliente
2. Detalhar Execution Protocol (serialização, validação, dispatcher)
3. Configurar CI/CD e testes automatizados em cada repositório
4. Documentar arquitetura e fluxos no README de cada repositório
5. Garantir rastreabilidade e reprodutibilidade completas