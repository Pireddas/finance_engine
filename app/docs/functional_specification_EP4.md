# Functional Specification — MVP Foundation (EP-4)

**Framework Padronizado de Comparação de Ativos Financeiros**  
**Arquivo:** `framework_back_end/docs/functional_specification_EP4.md`  
**Identificação:** FS-1.0  

**Origem:**  
- `business_requirements.md` (BR-4.4)  
- `evolutionary_phases.md` (EP-4)  
- `user_stories_EP4.md` (US-01 a US-05)

**Elaboração:** PMO / Especialista de Requisitos / Arquiteto de Software  
**Validação:** Product Owner / Gerência / Alta Gestão  
**Status:** Aprovado  
**Versão:** 1.0

---

## FS-1. Objetivo e Escopo
**Origem:** EP-4, BR-4.4

O objetivo desta especificação funcional é definir, de forma normativa e verificável, o comportamento da **Fundação Técnica obrigatória (MVP Foundation)** do framework.

Esta fase **não realiza cálculos financeiros**. Seu propósito exclusivo é estabelecer os mecanismos institucionais de controle, legitimidade e rastreabilidade que tornam válidas as execuções das fases subsequentes.

### Escopo Funcional
- **FS-1.1** — Implementar a estrutura do Backend e do Cliente.
- **FS-1.2** — Estabelecer o Protocolo de Execução e a Execution Identity.
- **FS-1.3** — Garantir governança mínima por meio de autorização explícita de métodos e versões.

---

## FS-2. Princípios Funcionais da Fase 1 (MVP Foundation)
**Origem:** EP-2, EP-4

- **FS-2.1 — Invalidade Institucional**  
  Qualquer execução realizada fora desta fundação técnica é considerada institucionalmente inválida.

- **FS-2.2 — Soberania do Backend**  
  O backend atua como orquestrador central, sendo responsável por validar identidades, permissões e condições de execução antes de qualquer processamento.

- **FS-2.3 — Inalterabilidade da Identidade**  
  A Execution Identity é o elo indivisível entre a solicitação, o processamento e qualquer resultado produzido futuramente.

---

## FS-3. Descrição das Funcionalidades

### FS-3.1 Estrutura de Backend Modular (US-01)
**Origem:** BR-4.4.1

O sistema deve ser organizado em camadas estritas, garantindo isolamento de responsabilidades e evolução controlada:

- **Application** — Casos de uso e orquestração de fluxos.
- **Domain** — Entidades centrais e regras de negócio essenciais.
- **Infrastructure** — Implementação de logging, persistência, segurança e conectores externos.

---

### FS-3.2 Protocolo de Execução e Dispatcher (US-02)
**Origem:** BR-4.4.2

Toda comunicação entre Cliente e Backend deve ocorrer exclusivamente por meio do **Execution Protocol**, composto por:

1. **Serialização** — Padronização formal dos parâmetros de entrada.
2. **Validação** — Verificação de integridade, completude e conformidade dos parâmetros.
3. **Dispatcher** — Orquestrador funcional responsável por direcionar a execução para o fluxo autorizado.

Nenhuma execução pode ocorrer fora deste protocolo.

---

### FS-3.3 Gestão de Identidade e Acesso (US-03)
**Origem:** BR-5.5, BR-4.4.3

- **Autenticação** — Identificação obrigatória da entidade solicitante.
- **Autorização por Roles** — Controle de acesso baseado em perfis institucionais.
- **Execution Identity** — Toda execução válida deve gerar ou validar um identificador único, persistente e rastreável.

---

### FS-3.4 Governança de Métodos e Versões (US-04)
**Origem:** BR-4.4.1, BR-4.4.4

- **Bloqueio Preventivo** — Execuções com métodos, fórmulas ou versões não homologadas devem ser impedidas antes de qualquer processamento.
- **Registro de Versão** — A versão exata do método autorizado deve ser vinculada de forma imutável à Execution Identity.

---

### FS-3.5 Auditoria Imutável e Interface CLI (US-05)
**Origem:** BR-4.4.3, BR-4.4.4

- **Logs Append-only** — Geração de registros técnicos que impeçam edição retroativa.
- **Trilha Técnica de Auditoria** — Os logs devem conter, no mínimo: quem executou, quando executou e o que foi executado.
- **Interface CLI** — Disponibilização de ferramenta de linha de comando para inspeção e rastreamento técnico das execuções.

---

### FS-3.6 Desempenho e Escalabilidade Operacional (US-06)
**Origem:** One-Pager Executivo (Impacto Operacional)

- **Capacidade de Carga:** O framework deve ser dimensionado para suportar uma volumetria inicial de 1.200+ execuções mensais, com capacidade de expansão para "Escala Industrial".
- **Tempo de Resposta (Overhead):** O processo de validação, autorização e registro de log não deve adicionar mais de 500ms ao tempo total de resposta da requisição.
- **Disponibilidade de Fundação:** Sendo a EP-4 o "Gate" obrigatório para qualquer análise, os serviços de Identidade e Auditoria devem possuir alta disponibilidade, garantindo que a governança não se torne um ponto de falha para a operação da Asset.
  
---

## FS-4. Dependências Funcionais
**Origem:** EP-4

- Nenhuma.  
Esta é a fase fundamental (Foundation) e constitui pré-requisito obrigatório para todas as fases subsequentes, incluindo o Core Calculation (EP-5).

---

## FS-5. Regras de Erro e Exceção
**Origem:** EP-4

1. **Identidade Ausente** — Solicitações sem Execution Identity válida devem ser bloqueadas imediatamente.
2. **Método não Homologado** — Tentativas de execução de métodos ou versões não autorizadas devem resultar em erro de conformidade.
3. **Falha de Log** — Se o sistema de auditoria (append-only) estiver indisponível, a execução não deve prosseguir.

---

## FS-6. Indicadores de Sucesso (KPIs)
**Origem:** EP-4

- 100% das execuções associadas a uma Execution Identity válida.
- Zero execuções com métodos ou versões não autorizados.
- Integridade total dos logs institucionais durante testes e validações da fundação.

---

## EPS-7. Performance e Resiliência do Protocolo

### EPS-7.1 Concorrência
O protocolo deve ser capaz de gerenciar múltiplas solicitações simultâneas (burst requests), garantindo que a geração de hashes de `Execution Identity` e a escrita em logs `Append-only` não gerem contenção de recursos ou bloqueios (deadlocks).

### EPS-7.2 Tratamento de Sobrecarga (Backpressure)
Caso o sistema atinja o limite de capacidade de escrita de auditoria, o protocolo deve interromper novas execuções com erro de "Sistema Sobrecarregado", impedindo que qualquer processamento ocorra sem o devido registro imutável.

---

## EPS-8. Regras de Erro e Bloqueio Normativo

1. **Identidade Ausente ou Inválida**
   → Bloqueio imediato. Status: `401 Unauthorized`.
2. **Método ou Versão Não Homologados**
   → Erro de conformidade. Status: `403 Forbidden`.
3. **Falha ou Indisponibilidade de Logging**
   → Aborto preventivo da execução. Status: `503 Service Unavailable`.
4. **Violação de Timeout de Governança**
   → Caso a validação de protocolo exceda o tempo limite, a execução é invalidada por segurança.
   
---

## Conformidade

A Fase 1 (MVP Foundation) equivale à instalação do sistema de segurança e à emissão de crachás de acesso. Antes de qualquer produção (cálculo), é necessário garantir que os acessos estejam controlados. Sem essa base, nenhuma operação possui validade institucional, legal ou técnica.

---
---
---

# Anexos


# Execution Protocol Specification — EPS-1.0

**Framework Padronizado de Comparação de Ativos Financeiros**

**Anexo 1:** `execution_protocol_specification`
**Identificação:** EPS-1.0
**Origem:**

* `business/business_requirements.md` (BR-4.4)
* `business/evolutionary_phases.md` (EP-4)
* `dev/docs/Fase_1/functional_specification.md` (FS-3.2, FS-3.3)
* `dev/docs/Fase_1/user_stories.md` (US-02, US-03)
  **Elaboração:** PMO / Especialista de Requisitos / Arquiteto de Software
  **Validação:** Product Owner / Gerência / Alta Gestão
  **Status:** Aprovado
  **Versão:** 1.0

---

## EPS-1. Objetivo do Documento

Este documento formaliza a **especificação técnica normativa** do **Execution Protocol** da **Fase 1 (EP-4 — MVP Foundation)**.

O Execution Protocol é o **contrato soberano** entre Cliente e Backend, responsável por garantir:

* legitimidade da execução;
* rastreabilidade técnica;
* reprodutibilidade institucional;
* bloqueio preventivo de execuções inválidas.

> Este documento **não cria novos requisitos**.
> Ele **materializa tecnicamente** o que já é obrigatório no FS-3.2 e FS-3.3.

---

## EPS-2. Escopo e Não-Escopo

### 2.1 Escopo

* Estrutura canônica da requisição de execução
* Validação estrutural e semântica
* Geração e validação da Execution Identity
* Dispatcher e roteamento controlado
* Integração obrigatória com logging append-only

### 2.2 Não-Escopo

* Cálculo de métricas financeiras
* Regras de negócio de análise
* Lógica estatística ou financeira
* Interface gráfica

---

## EPS-3. Princípios Normativos do Protocolo

### EPS-3.1 Obrigatoriedade

Toda execução **deve** trafegar exclusivamente pelo Execution Protocol.

### EPS-3.2 Invalidade Institucional

Qualquer execução realizada fora deste protocolo é considerada **institucionalmente inválida**.

### EPS-3.3 Soberania do Backend

O Backend é a autoridade final para validação, autorização e aceitação da execução.

### EPS-3.4 Inalterabilidade

A Execution Identity é indivisível e imutável após a validação inicial.

---

## EPS-4. Estrutura Canônica da Requisição

Toda solicitação enviada pelo Cliente ao Backend **deve** conter os seguintes blocos lógicos:

1. **Header Institucional**

   * identificação do cliente
   * versão do protocolo
   * timestamp

2. **Execution Context**

   * usuário ou entidade solicitante
   * roles declarados
   * ambiente (ex: dev, staging, prod)

3. **Governance Context**

   * método solicitado
   * versão do método
   * justificativa ou finalidade (quando aplicável)

4. **Payload de Execução**

   * parâmetros serializados
   * dados de entrada normalizados

---

## EPS-5. Fases do Execution Protocol

### EPS-5.1 Serialização

* Parâmetros devem ser convertidos para formato canônico.
* Tipos inválidos ou não suportados devem ser rejeitados.

### EPS-5.2 Validação Estrutural

* Verificação de presença de todos os blocos obrigatórios.
* Rejeição imediata em caso de inconsistência.

### EPS-5.3 Validação de Identidade

* Autenticação da entidade solicitante.
* Validação de roles e permissões.

### EPS-5.4 Governança e Autorização

* Verificação se o método solicitado está homologado.
* Verificação da versão autorizada.

### EPS-5.5 Dispatcher

* Roteamento controlado para o caso de uso autorizado.
* Nenhum acesso direto à camada de execução.

### EPS-5.6 Logging Obrigatório

* Registro append-only antes e após o dispatcher.
* Associação inequívoca com a Execution Identity.

---

## EPS-6. Execution Identity

### EPS-6.1 Definição

A Execution Identity é o identificador único e soberano de uma execução.

### EPS-6.2 Conteúdo Mínimo

* hash único da execução
* método e versão autorizados
* identidade do solicitante
* timestamp de validação

### EPS-6.3 Regras

* Gerada ou validada antes de qualquer processamento.
* Propagada por todo o fluxo de execução.
* Persistida em logs institucionais.

---

## EPS-7. Regras de Erro e Bloqueio

1. **Identidade Ausente ou Inválida**
   → Bloqueio imediato da execução.

2. **Método ou Versão Não Homologados**
   → Erro de conformidade institucional.

3. **Falha de Logging**
   → Execução abortada para preservar auditabilidade.

---

## EPS-8. Versionamento do Protocolo

* O Execution Protocol é versionado de forma explícita.
* Alterações incompatíveis exigem nova versão major.
* Versões antigas permanecem válidas enquanto homologadas pela governança.

---

## EPS-9. Relação com Fases Evolutivas

* EP-4: Define e torna obrigatório o Execution Protocol.
* EP-5+: Utilizam o protocolo sem alterá-lo.
* EP-8: Evidencia formalmente a aderência histórica ao protocolo.

