**Ata de Reunião — Definições Arquiteturais do Projeto Corporativo**

**Data:** `12/01/2026`  
**Local:** `Reunião Remota / Videoconferência`  
**Versão:** `1.0`  
**Elaboração:** `PMO / Especialista de Requisitos / Arquiteto de Software`  
**Validação:** `Product Owner / Gerência / Alta Gestão`  
  
---

## 1. Objetivo da Reunião

Definir estrutura de repositórios, raiz de código, protocolo de comunicação e fluxo do Execution Identity para os componentes do projeto corporativo, garantindo:

- Clareza institucional
- Rastreabilidade e reprodutibilidade
- Independência e soberania dos repositórios
- Base sólida para decisões futuras sobre regras, critérios e especificações

## 2. Participantes
|Nome|Cargo / Papel|
|-|-|
|-	|Arquiteto de Software / Especialista em Desenvolvimento|
|PMO	|Gerente de Projeto / Coordenador de Governança Técnica|
|PO	|Product Owner|
|Especialista de Requisitos	|Analista / Validação de Requisitosv|
|Engenheiro de Desenvolvimento	|Representante técnico do backend e cliente|

## 3. Pauta

1. Revisão da estrutura de repositórios do projeto corporativo
2. Definição da raiz de código (src/) e organização de packages
3. Configuração de Execution Protocol entre cliente e backend
4. Separação de responsabilidades entre backend, cliente e serviço de cálculo
5. Boas práticas de testes, imports e gerenciamento de dependências (Poetry, venv)
6. Estratégia de rastreabilidade e reprodutibilidade via Execution Identity
7. Critérios de governança e extensão para novos serviços
---

## 4. Definições e Decisões Tomadas
### 4.1 Estrutura de Repositórios

```
projeto_corporativo/               <- Container organizacional, NÃO repositório
 ├─ framework_back_end/            <- Repositório Back-End (src/ = raiz)
 ├─ framework_cliente/             <- Repositório Cliente / Protocolo (src/ = raiz)
 └─ framework_calculo_de_metricas/ <- Repositório Serviço de Cálculo (src/ = raiz)
```

> - Importante: projeto_corporativo/ é apenas ***container*** organizacional do projeto.  
> Ele não contém código executável e serve exclusivamente para agrupar os repositórios, documentação institucional e artefatos de governança, garantindo clareza, rastreabilidade e consistência arquitetural.

---

### 4.2 framework_back_end

- `src/` é a raiz do código
- Estrutura modular:
  - `application/` → Casos de uso e orquestração
  - `domain/` → Entidades e regras de negócio
  - `infrastructure/` → Conectores, logging, persistência e segurança
    - `connectors/` → Integração com serviços externos
    - `logging/` → Registro e auditoria
    - `persistence/` → Repositórios, loaders e gerenciamento de dados
    - `security/` → Autenticação, autorização, identity manager
  - `execution_protocol/` → Contrato e fluxo de Execution Identity
  - `governance/` → Constantes, padrões e configurações institucionais
- Backend é soberano, orquestra chamadas e valida Execution Identity
- Comunicação com cliente apenas via Execution Protocol
- Integração com serviço de cálculo para processamento de métricas
- Tests, scripts e CI/CD ficam fora de `src/`

---

### 4.3 framework_cliente

- src/ como raiz do código
- Estrutura modular: protocol/, cli/, web/, application/, domain/, governance/
- Serializa, valida e envia Execution Identity ao backend
- Independente de lógica de cálculo ou regras internas do backend
- CLI e Web compartilham protocolo e camada de aplicação
- Tests, scripts e CI/CD fora de src/

---

### 4.4 framework_calculo_de_metricas

- src/ como raiz do código
- Implementa apenas cálculos financeiros
Recebe dados do backend e retorna resultados estruturados
- Independente de clientes
- Pode ser evoluído separadamente

---

### 4.5 Execution Protocol

- Contrato formal entre cliente e backend
- Transporte independente de canal (CLI, Web, futuros clientes)
- Garante:
  - Rastreabilidade  
  - Reprodutibilidade   
  - Auditoria  
> Protocolo gera, valida ou propaga a Execution Identity

### 4.6 Convenção de Raiz (src/)

- Cada repositório define src/ como raiz do código Python
- Imports devem ser absolutos a partir de src/

---

### 4.7 Boas Práticas

- Separação clara entre produção e testes
- Todos os fluxos de execução passam pelo Execution Protocol
- Backend e Cliente são soberanos, versão controlada via Poetry
- Novos serviços podem ser adicionados ao mesmo nível, sem impacto cruzado
- Alterações estruturais ou de raiz exigem aprovação do time de arquitetura

---

#### 4.8 Fluxo de Execução Conceitual
```
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
---

### 4.9 Próximos Passos

- Definir regras funcionais e critérios de execução para backend e cliente
- Documentar Execution Protocol detalhado (serialização, validação, dispatcher)
- Garantir CI/CD e testes automatizados antes de evoluções funcionais

### 4.10 Observações

- Esse documento serve como referência institucional para próximos ciclos de desenvolvimento
- Todas decisões técnicas ou estruturais futuras devem seguir este padrão