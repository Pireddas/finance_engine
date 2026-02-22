# Acceptance Criteria — MVP Foundation **EP-4** (Fase 1)
Framework Padronizado de Comparação de Ativos Financeiros

Arquivo: framework_back_end/docs/acceptance_criteria_EP4.md  
Identificação: AC-1.0  

Origem:
- business_requirements.md (BR-4.4)
- evolutionary_phases.md (EP-4)
- functional_specification_EP4.md (FS-1.0)
- user_stories_EP4.md (US-01 a US-05)

Elaboração: PMO / Especialista de Requisitos / Arquiteto de Software  
Validação: Product Owner / Gerência / Alta Gestão  
Status: Aprovado  
Versão: 1.0  

---

## AC-1. Objetivo e Princípios da EP- (Fase 1)  
**Ref.: EP-4, BR-4.4, FS-1**

Este documento define os **Critérios de Aceitação formais** da Fase 1 — MVP Foundation, que constitui a **fundação técnica obrigatória e inegociável** do framework.

### AC-1.1
Estabelecer legitimidade institucional por meio de identidade, autorização e protocolo controlado.

### AC-1.2
Garantir que **nenhuma métrica financeira seja calculada** nesta fase, limitando o escopo à base técnica.

### AC-1.3
Determinar que qualquer execução realizada fora desta fundação seja considerada **institucionalmente inválida**.

---

## AC-2. Princípios Obrigatórios (Baseline Técnico)  
**Ref.: FS-2, EP-3**

### AC-2.1 — Soberania do Backend
O backend deve atuar como **orquestrador central** e autoridade final para validação, autorização e aceitação de execuções.

### AC-2.2 — Indivisibilidade da Identidade
A Execution Identity deve ser o **elo indivisível** entre solicitação, execução e qualquer resultado futuro.

### AC-2.3 — Obrigatoriedade do Protocolo
Toda execução deve trafegar **exclusivamente** pelo Execution Protocol, sem exceções técnicas ou operacionais.

---

## AC-3. Critérios de Aceitação Funcionais  
**Ref.: FS-3, US-01 a US-05**

### AC-3.1 — Estrutura de Backend Modular
- Existência comprovada das camadas `application/`, `domain/` e `infrastructure/` sob `src/`.
- Isolamento estrito de responsabilidades entre:
  - orquestração (application)
  - regras de negócio (domain)
  - serviços técnicos (infrastructure)

---

### AC-3.2 — Protocolo de Execução (Execution Protocol)
- Implementação funcional dos estágios:
  - Serialização
  - Validação
  - Dispatcher
- Bloqueio imediato de qualquer execução que tente:
  - ignorar o protocolo
  - acessar fluxos internos diretamente

---

### AC-3.3 — Gestão de Identidade e Acesso
- Autenticação e autorização baseadas em roles são obrigatórias.
- 100% das execuções bem-sucedidas devem gerar:
  - Execution Identity única
  - persistente
  - rastreável

---

### AC-3.4 — Governança de Métodos e Versões
- Bloqueio preventivo de métodos, fórmulas ou versões não homologadas.
- Vinculação **imutável** da versão do método autorizado à Execution Identity.

---

### AC-3.5 — Auditoria Técnica e Interface CLI
- Geração automática de logs em modo append-only.
- Logs devem impedir qualquer edição retroativa.
- Disponibilização de CLI técnica que permita:
  - inspeção do fluxo
  - rastreamento da execução
  - verificação de identidade e método autorizado

---

## AC-4. Critérios de Aceitação Não Funcionais (Qualidade)  
**Ref.: BR-4.4.4, FS-5**

### AC-4.1 — Imutabilidade de Logs
Caso o subsistema de auditoria (append-only) falhe ou esteja indisponível, o sistema deve **abortar a execução imediatamente**.

### AC-4.2 — Segurança de Identidade
Solicitações sem Execution Identity válida ou sem roles autorizados devem resultar em:
- erro de conformidade
- bloqueio da execução

### AC-4.3 — Performance e Escalabilidade (Sizing)
- **Overhead de Governança:** O tempo total gasto no Execution Protocol (identidade + validação + logging) não deve exceder **500ms** por requisição.
- **Concorrência:** O sistema deve processar múltiplas solicitações simultâneas sem perda de integridade de logs ou geração de duplicidade de `Execution Identity`.
- **Resiliência de Carga:** O sistema deve manter estabilidade sob carga projetada de **1.200+ execuções mensais** (Baseline do One-Pager + 100% de folga).
  
---

## AC-5. KPIs Mínimos para Aceitação da Fase 1  
**Ref.: EP-4, FS-6**

A Fase 1 é considerada formalmente entregue somente quando:

- **KPI-1:** 100% das execuções possuem Execution Identity válida.
- **KPI-2:** Zero execuções realizadas com métodos ou versões não autorizados.
- **KPI-3:** Integridade total dos logs institucionais comprovada.
- **KPI-4:** Tempo médio de resposta da camada de protocolo (overhead) inferior a **500ms**.
- **KPI-5:** Sucesso em teste de estresse simulando picos de demanda (concorrência) sem falhas de escrita no Audit Logger.
- 
---

## AC-6. Gate Formal de Saída da Fase  
**Ref.: EP-2**

A Fase 1 só pode ser encerrada após:

1. Verificação técnica da modularidade do backend conforme convenção `src/`.
2. Validação do fluxo completo do Execution Protocol (Cliente → Backend).
3. Homologação formal da governança mínima para autorização de métodos.

