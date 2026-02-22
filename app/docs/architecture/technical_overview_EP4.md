# Technical Overview — Fase 1 (MVP Foundation)
Framework Padronizado de Comparação de Ativos Financeiros

Arquivo: framework_back_end/docs/architecture/technical_overview_EP4.md  
Identificação: TO-1.0  

Origem:
- business_requirements.md (BR-4.4)
- evolutionary_phases.md (EP-4)
- functional_specification_EP4.md (FS-1.0)
- Anexo FS-1.0: execution_protocol_specification (EPS-1.0)

Elaboração: Arquiteto / Engenheiros de Desenvolvimento / Dono do Framework  
Validação: Arquiteto / Dono do Framework / PMO  
Status: Aprovado  
Versão: 1.0  

---

## TO-1. Objetivo e Escopo Técnico  
**Ref.: BR-4.4, EP-4, FS-1**

Este documento descreve a **implementação técnica da Fase 1 — MVP Foundation**, estabelecendo a infraestrutura mínima necessária para garantir legitimidade, controle e rastreabilidade institucional do framework.

### TO-1.1
Documentar a fundação técnica composta por:
- Backend modular
- Execution Protocol
- Identity Management
- Governança mínima

### TO-1.2
Assegurar que **nenhuma métrica financeira seja calculada** nesta fase.

### TO-1.3
Garantir que qualquer execução futura seja **rastreável, verificável e institucionalmente válida** por meio da fundação estabelecida.

---

## TO-2. Escopo da Implementação  
**Ref.: FS-3, EPS-5, EP-4**

A implementação técnica da Fase 1 está estruturada em cinco pilares obrigatórios:

- **TO-2.1 Estrutura Modular**  
  Organização do backend nas camadas `application`, `domain` e `infrastructure` sob a raiz `src/`.

- **TO-2.2 Execution Protocol**  
  Contrato formal e soberano de comunicação entre Cliente e Backend, com serialização e validação estrutural.

- **TO-2.3 Identity Management**  
  Autenticação, autorização baseada em roles e ciclo de vida completo da Execution Identity.

- **TO-2.4 Governança de Execução**  
  Mecanismos preventivos de bloqueio para métodos ou versões não homologados.

- **TO-2.5 Auditoria Imutável**  
  Sistema de logs em modo append-only, vinculado de forma indissociável à Execution Identity.

---

## TO-3. Componentes Técnicos Principais  
**Ref.: AO-4, EPS-4, EPS-6**

| Componente | Descrição Técnica |
|-----------|------------------|
| Execution Protocol | Contrato soberano que exige Header Institucional, Execution Context, Governance Context e Payload |
| Identity Manager | Geração e validação da Execution Identity (hash único, roles, timestamp) |
| Governance Module | Validador de conformidade para métodos e versões autorizadas |
| Audit Logger | Motor de registro imutável (append-only) do quem, quando e o quê |
| Modular Backend | Orquestrador soberano que isola domínio, aplicação e infraestrutura |

---

## TO-4. Fluxo Técnico de Execução  
**Ref.: AO-5, EPS-5**

O fluxo técnico da Fase 1 é **linear, causal e bloqueante**:

1. **Serialização**  
   O cliente estrutura os parâmetros conforme o Execution Protocol.

2. **Validação Estrutural**  
   O backend valida a presença e integridade de todos os blocos obrigatórios.

3. **Validação de Identidade**  
   Autenticação da entidade e verificação de roles autorizados.

4. **Governança**  
   Verificação formal de autorização do método e versão solicitados.

5. **Dispatcher**  
   Roteamento controlado para o fluxo autorizado, sem acesso direto à execução.

6. **Logging Append-only**  
   Registro imutável da operação, vinculado à Execution Identity.

---

## TO-5. Responsabilidades Técnicas  
**Ref.: AO-4, EPS-5**

- **framework_back_end**  
  Autoridade final para validação, autorização e geração de logs institucionais.

- **framework_cliente**  
  Responsável pela serialização correta e envio da requisição via protocolo soberano.

- **Execution Protocol**  
  Garantia de rastreabilidade e reprodutibilidade independente do canal de acionamento.

---

## TO-6. Restrições e Critérios de Sucesso  
**Ref.: AO-6, EPS-7, AC-5**

### TO-6.1 — Bloqueio de Cálculo
Qualquer tentativa de processamento financeiro nesta fase deve **abortar imediatamente a execução**.

### TO-6.2 — Integridade de Auditoria
Falha no subsistema de logs imutáveis implica bloqueio imediato da operação.

### TO-6.3 — Conformidade de Identidade
Execuções sem Execution Identity válida ou sem autorização resultam em erro de conformidade.

### KPI de Sucesso
- 100% das execuções com Execution Identity válida  
- Logs íntegros e imutáveis  
- Zero uso de métodos ou versões não autorizadas  

---

## TO-7. Estrutura de Domínios e Pastas  
**Ref.: AO-3.1**

```text
framework_back_end/
└── src/
    ├── application/              # Casos de uso e orquestração (Dispatcher)
    ├── domain/                   # Entidades e regras essenciais
    └── infrastructure/           # Implementações técnicas
        ├── security/             # Identity Manager (Auth / Roles)
        ├── logging/              # Audit Logger (Append-only)
        ├── execution_protocol/   # Contrato e Serialização
        └── governance/           # Validação de Métodos e Versões
```
