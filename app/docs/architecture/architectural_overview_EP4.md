# Architectural Overview — MVP Foundation EP-4 (Fase 1)

Framework Padronizado de Comparação de Ativos Financeiros

**Arquivo:** framework_back_end/architecture/architectural_overview_EP4.md
**Identificação:** AO-1.0
**Origens:**
 
* business_requirements.md (BR-4.4)
* evolutionary_phases.md (EP-4)
* functional_specification_EP4.md (FS-1.0)
* user_stories_EP4.md (US-01 a US-05)
* Anexo FS-1.0: execution_protocol_specification (EPS-1.0)

**Elaboração:** Arquiteto / Engenheiros de Desenvolvimento / Dono do Framework
**Validação:** Arquiteto / Dono do Framework / PMO
**Status:** Aprovado
**Versão:** 1.0

---

## AO-1. Objetivo do Documento

**Origem:** BR-4.4, EP-4, FS-1

Este documento apresenta a visão arquitetural da Fase 1 — MVP Foundation, detalhando a infraestrutura técnica mínima e inegociável necessária para garantir a legitimidade e rastreabilidade do framework.

* **AO-1.1:** Descrever a estrutura modular soberana do Backend e do Cliente.
* **AO-1.2:** Detalhar o funcionamento do Execution Protocol e da Execution Identity.
* **AO-1.3:** Estabelecer a base de governança para autorização de métodos e trilhas de auditoria.
* **AO-1.4:** Reiterar que nenhuma métrica financeira é calculada nesta fase.

---

## AO-2. Princípios Arquiteturais da Fase 1

**Origem:** FS-2, EPS-3, AC-2

* **AO-2.1 Soberania do Backend:** O backend atua como orquestrador central e autoridade final para validação e autorização.
* **AO-2.2 Invalidade Institucional:** Qualquer execução realizada fora deste protocolo ou fundação é considerada nula e sem valor legal.
* **AO-2.3 Indivisibilidade da Identidade:** A Execution Identity é o elo imutável entre o solicitante e o processamento.
* **AO-2.4 Rigor Protocolar:** Toda comunicação entre Cliente e Backend trafega obrigatoriamente pelo Execution Protocol.

---

## AO-3. Camadas Arquiteturais — Visão de Fundação

**Origem:** FS-3, EPS-4

### AO-3.1 Camada de Backend (`framework_back_end`)

Estrutura modular com `src/` como raiz:

* **Application:** Orquestração de fluxos e casos de uso.
* **Domain:** Entidades centrais e regras essenciais de negócio.
* **Infrastructure:** Persistência, segurança, conectores e logging.

### AO-3.2 Camada de Cliente (`framework_cliente`)

Responsável por interagir com o usuário e formalizar a requisição:

* **CLI/Application:** Interface técnica de linha de comando para acionamento e inspeção.
* **Protocol Layer:** Serialização e envio de dados para o backend.

### AO-3.3 Camada de Protocolo (Execution Protocol)

Contrato soberano de transporte, validação e roteamento que une Cliente e Backend.

---

## AO-4. Componentes da Fase 1 e Responsabilidades

**Origem:** FS-3, EPS-5, EPS-6

| Componente         | Função Principal                                                  | Vínculo de Negócio |
| ------------------ | ----------------------------------------------------------------- | ------------------ |
| Execution Protocol | Serialização, validação e roteamento (Dispatcher)                 | BR-4.4.2           |
| Identity Manager   | Autenticação, autorização (roles) e geração da Execution Identity | BR-5.5 / BR-4.4.3  |
| Governance Module  | Validação de métodos e versões homologadas                        | BR-4.4.1           |
| Audit Logger       | Registro imutável (append-only) de auditoria                      | BR-4.4.4           |
| Modular Backend    | Infraestrutura técnica de suporte                                 | BR-4.4.1           |

---

## AO-5. Fluxo Arquitetural da Fase 1

**Origem:** EPS-5

Fluxo linear, sequencial e bloqueante:

1. **Serialização:** Cliente padroniza parâmetros de entrada.
2. **Validação Estrutural:** Backend valida integridade e obrigatoriedade dos campos.
3. **Validação de Identidade:** Autenticação e autorização por roles.
4. **Governança:** Verificação de método e versão homologados.
5. **Dispatcher:** Roteamento controlado do fluxo.
6. **Logging Append-only:** Registro imutável vinculado à Execution Identity.

---

## AO-6. Restrições Arquiteturais

**Origem:** FS-5, EPS-7, AC-4

* **AO-6.1 Ausência de Cálculo:** Qualquer tentativa de cálculo financeiro deve abortar a execução.
* **AO-6.2 Falha de Log:** Indisponibilidade do sistema de auditoria bloqueia a execução.
* **AO-6.3 Bloqueio de Identidade:** Solicitações sem identidade válida ou roles autorizados resultam em erro de conformidade.

---

## AO-7. Critérios de Sucesso Técnico da Fase 1

**Origem:** EP-4, FS-6, AC-5

* **KPI-1:** 100% das execuções associadas a uma Execution Identity válida.
* **KPI-2:** Zero execuções com métodos ou versões não autorizados.
* **KPI-3:** Integridade total comprovada dos logs institucionais.

---

## AO-8. Analogia Arquitetural da Fase 1

A Fase 1 equivale à instalação do sistema de segurança e da fundação estrutural de uma fábrica. Antes de qualquer produção (cálculo da Fase 2), é obrigatório garantir que o protocolo funcione, os logs estejam ativos e apenas entidades autorizadas tenham acesso ao backend. Sem essa base, qualquer operação é considerada clandestina e sem validade institucional.

---

## AO-9. Dimensionamento e Performance (Sizing)

**Origem:** Business Case / Impacto Operacional 6.1

A arquitetura da Fase 1 deve prever a volumetria baseada no esforço analítico atual (~640h/mês), garantindo folga operacional para a escalabilidade prometida nas fases futuras.

* **AO-9.1 Capacidade Nominal:** O backend deve suportar o processamento de requisições de identidade e log para um volume de até **1.200+ comparações/mês** (Baseline atual + 100% de folga imediata).
* **AO-9.2 Concorrência:** Suporte a execuções simultâneas sem degradação do `Identity Manager` ou do `Audit Logger`, prevendo picos de fechamento de mercado.
* **AO-9.3 Latência de Protocolo:** O overhead introduzido pelo *Execution Protocol* (validação + log) deve ser inferior a **200ms**, garantindo que a governança não se torne um gargalo de performance.
* **AO-9.4 Escalabilidade Horizontal:** Os componentes de `Infrastructure` (API e DB de Logs) devem permitir crescimento horizontal para suportar o plano de "Escala Industrial" da EP-8 sem refatoração de código.

---
