# Planned Unit Tests — Fase 1: MVP Foundation
**Arquivo:** `framework_back_end/testing/planned_unit_tests_EP4.md`  
**Origens:**  
- `business_requirements.md (BR-4.4)`  
- `evolutionary_phases.md (EP-4)`  
- `functional_specification_EP4.md (FS-1.0)`  
- `architectural_overview_EP4.md (AO-1.0)`  
- `acceptance_criteria_EP4.md (AC-1.0)`  

**Identificação:** PUT-1.0  
**Elaboração:** QA / Engenheiros de Desenvolvimento  
**Validação:** PMO / Arquiteto / Product Owner  
**Status:** Aprovado  
**Versão:** 1.0  

---

## 1. Objetivo e Princípios
**Origem:** AC-1.1, AC-1.2, FS-1.0  

Garantir cobertura técnica total dos componentes da Fundação Técnica, assegurando que a base institucional seja inegociável e que:  
- **Inexistência de Cálculo:** Nenhuma lógica financeira seja processada nesta fase.  
- **Soberania do Backend:** O backend valide rigorosamente todas as identidades e condições de execução antes de qualquer fluxo.  
- **Integridade de Auditoria:** Nenhuma ação ocorra sem o devido registro imutável.

---

## 2. Mapeamento de Componentes e Responsabilidades
**Origem:** AO-4, EPS-5, TO-3  

| Componente         | Regras Relacionadas          | Foco do Teste Unitário |
|-------------------|-----------------------------|-----------------------|
| Modular Backend    | BR-4.4.1, FS-3.1           | Isolamento de camadas (src/) e imports absolutos. |
| Execution Protocol | BR-4.4.2, EPS-4            | Serialização e validação de blocos obrigatórios. |
| Identity Manager   | BR-5.5, FS-3.3             | Autenticação, autorização (roles) e geração de hash único. |
| Governance Module  | BR-4.4.1, FS-3.4           | Validação de métodos e versões autorizados. |
| Audit Logger       | BR-4.4.4, FS-3.5           | Escrita append-only e associação com Execution Identity. |

---

## 3. Detalhamento dos Casos de Teste

### 3.1 Modular Backend — Estrutura Soberana
- **PUT-01.1:** Verificar a existência das pastas `application/`, `domain/` e `infrastructure/` sob a raiz `src/`.  
- **PUT-01.2:** Validar que todos os imports internos utilizam caminhos absolutos a partir de `src/`.  
- **PUT-01.3:** Bloquear a execução se houver tentativa de inclusão de lógica fora das camadas definidas.  

### 3.2 Execution Protocol — Serialização e Contrato
- **PUT-02.1:** Validar a rejeição de requisições que não contenham os 4 blocos obrigatórios: Header Institucional, Execution Context, Governance Context e Payload.  
- **PUT-02.2:** Testar o bloqueio imediato de tentativas de bypass do protocolo via chamadas diretas a casos de uso.  
- **PUT-02.3:** Validar erro PROTO-001 para versões de protocolo incompatíveis.  

### 3.3 Identity Manager — Legitimidade e Roles
- **PUT-03.1:** Garantir a geração de uma Execution Identity única (UUID/Hash) com timestamp UTC para toda requisição válida.  
- **PUT-03.2:** Validar o bloqueio (AUTH-001) para usuários sem role definido ou com roles inválidos.  
- **PUT-03.3:** Assegurar que a identidade seja propagada por todo o pipeline técnico.  

### 3.4 Governance Module — Blindagem de Métodos
- **PUT-04.1:** Bloquear preventivamente (GOV-001) a execução de qualquer método ou versão não homologado formalmente.  
- **PUT-04.2:** Validar a vinculação imutável da versão do método autorizado à Execution Identity gerada.  

### 3.5 Audit Logger — Auditoria Imutável
- **PUT-05.1:** Validar que logs são gerados em modo append-only, impedindo deleção ou edição.  
- **PUT-05.2:** Testar o aborto imediato da execução caso o subsistema de log esteja indisponível ou apresente falha de escrita.  
- **PUT-05.3:** Verificar a associação inequívoca entre cada registro de log e sua respectiva Execution Identity.  

### 3.6 Regras de Escopo e Performance
- **PUT-06.1:** Bloqueio de Cálculo: Garantir que qualquer tentativa de processamento financeiro nesta fase resulte em aborto imediato (SCOPE-001).  
- **PUT-06.2:** Validar que o overhead introduzido pelo protocolo (validação + log) seja inferior a 500ms.  

---

## 4. Critérios de Sucesso da Validação
**Origem:** EP-4, AC-5  

O plano de testes unitários da Fase 1 é considerado aprovado se:  
1. **Cobertura de Fundação:** 100% das execuções possuem uma Execution Identity válida associada.  
2. **Determinismo Institucional:** Mesmas entradas resultam em trilhas de auditoria consistentes.  
3. **Pureza Técnica:** Zero execuções realizadas com métodos não autorizados ou cálculos financeiros.  
4. **Resiliência:** Sucesso na escrita de logs sob simulação de múltiplas solicitações simultâneas sem deadlocks ou duplicidade de hashes.
