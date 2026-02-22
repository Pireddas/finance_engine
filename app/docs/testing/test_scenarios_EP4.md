# Test Scenarios — MVP Foundation (EP-4)

**Framework Padronizado de Comparação de Ativos Financeiros**  
**Fundação Técnica:** Backend, Protocolo, Identidade e Governança  

**Arquivo:** `framework_back_end/testing/test_scenarios_EP4.md`  

**Origem:**
- `functional_specification_EP4.md` (FS-1.0)
- `evolutionary_phases.md` (EP-4)
- `acceptance_criteria_EP4.md` (AC-1.0)

**Identificação:** TS-1.0  
**Elaboração:** QA / Arquiteto de Software  
**Validação:** Product Owner / PMO / Dono do Framework  
**Status:** Aprovado  
**Versão:** 1.0  

---

## TS-1. Objetivo do Documento

Definir os cenários de teste obrigatórios para a **Fase 1 (EP-4)**, garantindo que a fundação técnica seja **inegociável, legítima e rastreável** antes de qualquer integração com serviços de cálculo.

---

## TS-2. Escopo dos Cenários

Os cenários de teste cobrem os pilares da fundação técnica estabelecida para a fase:

- Estrutura Modular do Backend  
- Protocolo de Execução (Execution Protocol)  
- Gestão de Identidade (Identity Management)  
- Governança de Métodos e Versões  
- Auditoria Imutável (Logs Append-only)  

---

## TS-3. Cenários de Teste Funcionais

### TS-3.1 Estrutura e Backend Modular

#### TS-3.1.1 Integridade da Estrutura Modular  
**Origem:** FS-3.1, US-01, AC-3.1  

- **Objetivo:** Verificar a existência das camadas obrigatórias.  
- **Validação:** Confirmar a presença das pastas `application/`, `domain/` e `infrastructure/` sob a raiz `src/`.  
- **Regra:** Rejeitar qualquer código fora da convenção ou com imports relativos fora da raiz.

---

### TS-3.2 Execution Protocol e Serialização

#### TS-3.2.1 Validação de Blocos Obrigatórios  
**Origem:** FS-3.2, EPS-4, AC-3.2  

- **Objetivo:** Garantir que a requisição contenha todos os blocos do protocolo.  
- **Validação:** Enviar requisições sem Header Institucional, Execution Context, Governance Context ou Payload.  
- **Resultado Esperado:** Bloqueio imediato e erro de serialização para requisições incompletas.

#### TS-3.2.2 Bloqueio de Bypass do Protocolo  
**Origem:** ADR-002, AC-3.2  

- **Objetivo:** Impedir chamadas diretas a fluxos internos.  
- **Validação:** Tentar acessar casos de uso ignorando o Dispatcher.  
- **Resultado Esperado:** Invalidade institucional e bloqueio da execução.

---

### TS-3.3 Identidade e Acesso

#### TS-3.3.1 Geração da Execution Identity  
**Origem:** FS-3.3, EPS-6, ADR-003  

- **Objetivo:** Garantir a criação de um elo indivisível para a execução.  
- **Validação:** Confirmar que 100% das execuções bem-sucedidas geram um hash único e persistente.  
- **Resultado Esperado:** Registro da identidade vinculado ao usuário e ao timestamp.

#### TS-3.3.2 Autorização por Roles  
**Origem:** US-03, FS-3.3  

- **Objetivo:** Validar controle de acesso.  
- **Validação:** Simular solicitações com roles não autorizadas.  
- **Resultado Esperado:** Erro de conformidade e bloqueio da execução.

---

### TS-3.4 Governança e Blindagem

#### TS-3.4.1 Bloqueio de Métodos Não Homologados  
**Origem:** FS-3.4, US-04, AC-3.4  

- **Objetivo:** Impedir o uso de métodos ou versões não autorizadas.  
- **Validação:** Tentar executar método com versão diferente da homologada.  
- **Resultado Esperado:** Bloqueio preventivo antes de qualquer processamento.

#### TS-3.4.2 Proibição de Cálculos Financeiros  
**Origem:** EP-4, AO-6.1, AC-1.2  

- **Objetivo:** Garantir a pureza técnica da Fase 1.  
- **Validação:** Tentar disparar qualquer lógica de cálculo financeiro.  
- **Resultado Esperado:** Aborto imediato da execução.

---

### TS-3.5 Auditoria e CLI

#### TS-3.5.1 Imutabilidade e Append-only  
**Origem:** FS-3.5, ADR-004, AC-4.1  

- **Objetivo:** Validar a integridade da trilha de auditoria.  
- **Validação:** Simular falha na escrita do log institucional.  
- **Resultado Esperado:** Aborto imediato da execução para preservar a auditabilidade.

#### TS-3.5.2 Inspeção via CLI Técnica  
**Origem:** US-05, AC-3.5  

- **Objetivo:** Validar a ferramenta de rastreamento técnico.  
- **Validação:** Utilizar a CLI para recuperar o histórico de uma Execution Identity.  
- **Resultado Esperado:** Exibição íntegra do log contendo **quem**, **quando** e **o que** foi executado.

---

### TS-3.6 Performance e Resiliência (Sizing)

#### TS-3.6.1 Teste de Estresse e Concorrência
**Origem:** One-Pager 6.1, AO-9.2, AC-4.3

- **Objetivo:** Garantir a integridade institucional sob alta demanda.
- **Validação:** Simular 50+ requisições simultâneas de geração de identidade e log (pico de fechamento).
- **Resultado Esperado:** 100% de sucesso na escrita dos logs; zero duplicidade de hashes; sem travamento de banco de dados (deadlock).

#### TS-3.6.2 Validação de Overhead do Protocolo
**Origem:** AO-9.3, AC-5 (KPI-4)

- **Objetivo:** Garantir que a governança não prejudique a produtividade.
- **Validação:** Medir o tempo entre o envio da requisição e o recebimento da `Execution Identity`.
- **Resultado Esperado:** Tempo de resposta médio (overhead) inferior a 500ms.
  
---

## TS-4. Regras de Governança dos Testes

**Origem:** EP-2, AC-5  

1. **Fundação Obrigatória:** Nenhum cenário de teste de fases futuras pode ser validado sem aprovação total da Fase 1.  
2. **Determinismo Institucional:** Execuções com os mesmos parâmetros devem gerar trilhas de auditoria consistentes.  
3. **KPI de Aceitação:**  
   - 100% das execuções com Execution Identity válida  
   - Zero métodos não autorizados  
   - Integridade total dos logs institucionais  
4. **Resiliência de Escala:** Os testes de aceitação devem incluir obrigatoriamente uma rodada de carga que valide o processamento de volume compatível com a "Escala Industrial" prevista para a EP-8.
