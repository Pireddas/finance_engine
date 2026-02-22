# Test Cases — MVP Foundation (EP-4)
**Framework Padronizado de Comparação de Ativos Financeiros**

**Arquivo:** `framework_back_end/testing/test_cases_EP4.md`  
**Identificação:** TC-1  

**Origens:**  
- `test_scenarios.md`  
- `functional_specification_EP4.md`  
- `business_requirements.md (BR-4.4)`  
- `acceptance_criteria_EP4.md`  

**Elaboração:** QA / Especialista de Requisitos  
**Validação:** Product Owner / PMO  
**Status:** Alinhado com a Governança de Testes  
**Versão:** 1.0  

---

## TC-1. Objetivo do Documento

Detalhar os casos de teste funcionais da **Fase 1 — MVP Foundation**, validando a base técnica inegociável do framework (Backend, Protocolo, Identidade e Governança), assegurando que **nenhuma métrica financeira seja calculada ou exposta nesta fase**.

---

## TC-2. Estrutura dos Casos de Teste

Cada caso de teste deve conter obrigatoriamente:

- ID  
- Cenário de Origem (TS)  
- Vínculo de Negócio (BR / EP)  
- Vínculo Funcional (FS)  
- Pré-condições  
- Entradas  
- Passos  
- Resultado Esperado (com status, código de erro e efeito colateral esperado)

---

## TC-3. Casos de Teste Funcionais

### TC-3.1 — Integridade da Estrutura Modular (Backend)

- **Cenário de Origem:** TS-3.1.1  
- **Vínculo de Negócio:** BR-4.4.1  
- **Vínculo Funcional:** FS-3.1  
- **Pré-condições:** Repositório `framework_back_end` inicializado.  

**Passos:**  
1. Acessar a raiz do código em `src/`.  
2. Verificar a existência das pastas `application/`, `domain/` e `infrastructure/`.  
3. Verificar tentativa de inclusão de código fora dessas camadas.  

**Resultado Esperado:**  
- Estrutura conforme arquitetura modular definida.  
- Execução bloqueada.  
- **Erro:** `ARCH-001` — Violação de arquitetura modular.

---

### TC-3.2 — Validação Estrutural do Execution Protocol

- **Cenário de Origem:** TS-3.2.1  
- **Vínculo de Negócio:** BR-4.4.2  
- **Vínculo Funcional:** FS-3.2  

**Passos:**  
1. Enviar requisição sem **Header Institucional**.  
2. Enviar requisição sem **Governance Context**.  
3. Enviar requisição com versão de protocolo incompatível.  

**Resultado Esperado:**  
- Rejeição imediata da requisição.  
- **Erro:** `PROTO-001` — Estrutura inválida.  
- Nenhum log de execução funcional criado.

---

### TC-3.3 — Controle de Schema e Campos Não Reconhecidos

- **Cenário de Origem:** TS-3.2.2  
- **Vínculo de Negócio:** BR-4.4.2  
- **Vínculo Funcional:** FS-3.2  

**Passos:**  
1. Enviar requisição com campo extra não documentado.  
2. Enviar requisição com schema obsoleto.  

**Resultado Esperado:**  
- Rejeição por inconsistência de schema.  
- **Erro:** `PROTO-002` — Schema não homologado.

---

### TC-3.4 — Geração e Propagação da Execution Identity

- **Cenário de Origem:** TS-3.3.1  
- **Vínculo de Negócio:** BR-5.5  
- **Vínculo Funcional:** FS-3.3  
- **Pré-condições:** Usuário autenticado com role válido.  

**Resultado Esperado:**  
- Execution Identity única (UUID/hash).  
- Timestamp UTC.  
- Registro obrigatório em log append-only.  
- **Erro em falha:** `EXEC-001`.

---

### TC-3.5 — Testes Negativos de Autorização

- **Cenário de Origem:** TS-3.3.2  
- **Vínculo de Negócio:** BR-4.4.3  
- **Vínculo Funcional:** FS-3.3  

**Passos:**  
1. Usuário sem role definido.  
2. Usuário com role inválido.  
3. Usuário válido tentando método não autorizado.  

**Resultado Esperado:**  
- Execução bloqueada.  
- **Erro:** `AUTH-001` — Acesso não autorizado.

---

### TC-3.6 — Bloqueio de Métodos Não Homologados

- **Cenário de Origem:** TS-3.4.1  
- **Vínculo de Negócio:** BR-4.4.1  
- **Vínculo Funcional:** FS-3.4  

**Resultado Esperado:**  
- Execução bloqueada preventivamente.  
- **Erro:** `GOV-001` — Método não homologado.

---

### TC-3.7 — Aborto por Falha de Auditoria (Append-only)

- **Cenário de Origem:** TS-3.5.1  
- **Vínculo de Negócio:** BR-4.4.4  
- **Vínculo Funcional:** FS-3.5  

**Cenários:**  
- Indisponibilidade do log  
- Timeout de escrita  
- Tentativa de retry  

**Resultado Esperado:**  
- Execução abortada.  
- **Erro:** `AUD-001`.  
- Nenhuma resposta de sucesso retornada.

---

### TC-3.8 — Idempotência e Replay de Execução

- **Cenário de Origem:** TS-3.6.1  
- **Vínculo de Negócio:** BR-4.4.5  
- **Vínculo Funcional:** FS-3.6  

**Passos:**  
1. Reexecutar requisição com mesma Execution Identity.  

**Resultado Esperado:**  
- Rejeição do replay.  
- **Erro:** `EXEC-002` — Execução duplicada.

---

### TC-3.9 — Concorrência Básica

- **Cenário de Origem:** TS-3.6.2  
- **Vínculo de Negócio:** BR-4.4.5  
- **Vínculo Funcional:** FS-3.6  

**Resultado Esperado:**  
- Execution Identities distintas.  
- Logs íntegros e isolados.  
- Nenhuma colisão de estado.

---

### TC-3.10 — Proibição de Cálculos Financeiros na Fase 1

- **Cenário de Origem:** TS-3.4.2  
- **Vínculo de Negócio:** EP-4 (Escopo)  
- **Vínculo Funcional:** FS-1.0  

**Resultado Esperado:**  
- Execução abortada.  
- **Erro:** `SCOPE-001` — Cálculo fora do escopo da fundação.

---

### TC-3.11 — Resiliência sob Carga (Stress Test)

- **Cenário de Origem:** TS-3.6.1
- **Vínculo de Negócio:** Visão Global do Programa (Escalabilidade)
- **Vínculo Funcional:** FS-3.6
- **Pré-condições:** Ambiente de staging configurado com simulação de carga.

**Passos:**
1. Disparar rajada (burst) de 50 requisições simultâneas em intervalo de 1 segundo.
2. Monitorar tempo de resposta e escrita no log.

**Resultado Esperado:**
- 100% das requisições com `Execution Identity` gerada.
- Zero falhas de concorrência no `Audit Logger`.
- Tempo de resposta (P95) inferior a 500ms.
- **Erro em falha:** `PERF-001` — Latência excedida ou falha de concorrência.

---

### TC-3.12 — Integridade de Log sob Indisponibilidade Parcial

- **Cenário de Origem:** TS-3.5.1
- **Vínculo Funcional:** FS-5.3 (Falha de Log)

**Passos:**
1. Simular lentidão (latência artificial) de 2.000ms na camada de persistência de log.
2. Tentar realizar execução via protocolo.

**Resultado Esperado:**
- O sistema deve respeitar o timeout e abortar a execução.
- Garantir que a regra "No Log, No Execution" seja soberana.
- **Erro:** `AUD-002` — Timeout de auditoria.
- 
---

## TC-4. Regras Gerais de Execução (Governança)

1. **Fundação Primeiro**  
   Nenhum teste das fases posteriores pode ser executado se a Fase 1 falhar.

2. **Causalidade Obrigatória**  
   Nenhuma execução é válida sem log append-only associado.

3. **Determinismo**  
   Mesmas entradas ⇒ mesmas trilhas de auditoria.

4. **Isolamento de Ambiente**  
   Testes não devem contaminar execuções subsequentes.

5. **Critério de Stress:** A Fase 1 só será considerada aprovada se superar o teste de concorrência (TC-3.11) sem perda de pacotes de auditoria, garantindo a escala industrial prometida ao Board.
