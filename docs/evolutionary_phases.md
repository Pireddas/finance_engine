Arquivo: evolutionary_phases.md  
Elaboração: Especialista de Requisitos  
Validação: Gerência / Alta Gestão  
Status: Aprovado  
Versão: 1.3

# Evolutionary Phases — Framework de Comparação de Ativos Financeiros

---

## EP-1. Objetivo do Documento

Este documento define as **fases evolutivas** do framework de comparação de ativos financeiros, com foco em:

- Entrega incremental de valor
- Estabilização do backend, protocolo, identidade e governança
- Integração com serviço de cálculo
- Disponibilização de interface web
- Adição de métricas avançadas, score e ranking
- Auditoria, escalabilidade e integração institucional

Serve como **roadmap oficial do produto**, garantindo evolução incremental, governada e mensurável.

---

## EP-2. Princípios de Evolução

- Cada fase entrega valor utilizável, independente e testável.
- Nenhuma fase depende de funcionalidades futuras não entregues.
- Backend, Protocolo, Identidade e Governança mínima são pré-requisitos obrigatórios.
- Evoluções não podem alterar resultados consolidados do MVP.
- KPIs claros definem sucesso; opiniões não são critérios.

---

## EP-3. Visão Geral das Fases

> **Nota Institucional:**  
> A governança é iniciada no EP-4 e evolui progressivamente até o EP-8, onde atinge seu nível máximo de maturidade institucional.

| Fase | Identificador | Nome | Objetivo Principal | Dependência |
|-----:|---------------|----------------------|--------------------|-------------|
| 1 | EP-4 | MVP Foundation | Estabelecer Backend, Protocolo, Identidade e Governança mínima. | Nenhuma |
| 2 | EP-5 | Core Calculation | Integrar o serviço de cálculo (Métricas do MVP). | EP-4 e BR-4.1 |
| 3 | EP-6 | Advanced Analytics | Integrar VaR, CVaR, Score e Ranking. | EP-5 e BR-4.2 |
| 4 | EP-7 | Visual Delivery | Disponibilizar interface Web para o MVP. | EP-5 e EP-6 |
| 5 | EP-8 | Governance & Scale | Evidenciar formalmente governança, rastreabilidade e correção dos cálculos para auditoria externa. | EP-5 |

---

## EP-4. — MVP Foundation  
**Ref. BR-4.4 — Governança e Auditoria Avançada (Fundação Técnica)**

*(Backend + Protocolo + Identidade + Governança mínima)*

### Alinhamento com Business Requirements
Este EP implementa a **base técnica obrigatória** para viabilizar futuramente os requisitos de governança definidos em:

- **BR-4.4.1** Versionamento formal de parâmetros  
- **BR-4.4.2** Snapshot da base de dados utilizada  
- **BR-4.4.3** Histórico completo de execuções  
- **BR-4.4.4** Trilhas de auditoria completas  

> Nota:  
> O EP-4 **não entrega auditoria avançada**.  
> Ele cria exclusivamente as **condições técnicas mínimas e inegociáveis** para que auditoria e evidência sejam possíveis sem retrabalho ou quebra futura.

### Objetivo
Estabelecer a base institucional obrigatória para qualquer execução futura,
garantindo identidade forte, legitimidade, controle de autorização
e rastreabilidade técnica.

> Nenhuma métrica financeira é calculada nesta fase.  
> **Qualquer execução fora desta fundação é considerada inválida.**

### Escopo
- Backend modular: `application/`, `domain/`, `infrastructure/`.
- Execution Protocol operacional: serialização, validação e dispatcher.
- Identity Management: autenticação, autorização e roles.
- Governança mínima (condição de execução):
  - validação formal de execução permitida
  - versionamento e autorização explícita de métodos
- Logging e auditoria básica (append-only).
- Fluxo de execução rastreável via CLI técnica.

### KPIs da Fase
- 100% das execuções associadas a uma Execution Identity válida.
- Nenhuma execução sem método autorizado.
- Logs institucionais gerados para todas as execuções.


---

## EP-5. — Integração com Serviço de Cálculo (Core)  
**Ref. BR-4.1 — MVP — Comparação Confiável e Reprodutível**  
**Ref. BR-4.1.1.4 — O sistema deve calcular, no mínimo, as seguintes métricas:**  
  `Retorno acumulado, CAGR, Volatilidade anualizada, Drawdown máximo, Sharpe Ratio e Correlação`  
**Ref. BR-4.1.1.8 — O sistema deve aceitar solicitação de cálculo apenas via `Token API Key`.**
**Ref. BR-4.1.1.9 — Integrar o backend ao serviço de cálculo.**

### Alinhamento com Business Requirements
Este EP operacionaliza integralmente os requisitos do MVP definidos em:

- **BR-4.1.1.1 → BR-4.1.1.7** (métricas, automação, relatório e metadados)
- **BR-5.1** Padrão mínimo aceitável de análise  
- **BR-5.4** Imutabilidade de resultados numéricos  
- **BR-5.5** Obrigatoriedade de Execution Identity válida  

> Este é o primeiro EP que entrega **valor de negócio direto**.  
> Antes disso há fundação. Depois disso há evolução.

### Objetivo
Executar métricas financeiras exclusivamente dentro da governança,
identidade e protocolo estabelecidos no EP-4.

> O serviço de cálculo **não define governança**  
> e **não executa métodos não previamente autorizados**.

### Escopo
- Integração com `framework_calculo_de_metricas`.
- Execução automatizada das métricas:
  - Retorno acumulado
  - CAGR
  - Volatilidade
  - Drawdown
  - Sharpe
  - Correlação
- Rastreabilidade completa de inputs, outputs e hash da execução.
- Execução restrita a métodos, versões e parâmetros aprovados pela governança.

### Dependências
- EP-4 (MVP Foundation).

### KPIs da Fase
- 100% das análises executadas sob Execution Identity válida.
- Integridade do hash validada entre backend e serviço de cálculo.
- Validação cruzada com casos de referência conhecidos.
- Pesos e regras versionados e auditáveis.
- Solicitação de cálculo aceita apenas via `Token API Key`.



---

## EP-6. — Advanced Analytics  
**Ref. BR-4.2 — Métricas de Risco  
Ref. BR-4.3 — Score, Ranking e Suporte à Decisão**

*(Risco, Score e Ranking)*

### Alinhamento com Business Requirements
Este EP implementa as funcionalidades previstas em:

- **BR-4.2.x** Métricas de risco (VaR, CVaR, múltiplos horizontes)
- **BR-4.3.x** Score agregado, ranking e classificação visual

> Conforme **BR-3.4**, nenhuma métrica do MVP é alterada.  
> Este EP apenas **complementa** análises já consolidadas.

### Objetivo
Expandir a capacidade analítica mantendo integralmente
as regras de governança, identidade e rastreabilidade já estabelecidas.

### Escopo
- Cálculo de VaR, CVaR e múltiplos horizontes temporais.
- Algoritmo de Score agregado por ativo.
- Ranking automático com pesos versionados.
- Regras formais previamente aprovadas pela governança institucional.

### Dependências
- EP-5 (Core Calculation).

### KPIs da Fase
- Métricas de risco presentes em 100% das novas análises.
- Resultados consistentes com premissas formalmente documentadas e versionadas.
- Pesos e regras versionados e auditáveis.

---

## EP-7. — Front-End Visual Web  
**Ref. BR-4.5.1 — Interface Gráfica**

### Alinhamento com Business Requirements
Este EP atende ao requisito de interface gráfica previsto em:

- **BR-4.5.1** Interface gráfica

> APIs, integrações e escala institucional não fazem parte deste EP.

### Objetivo
Disponibilizar interface amigável para consumo e validação institucional.

> A interface Web não introduz lógica de cálculo, 
> regras de decisão ou transformação de métricas.

### Escopo
- Interface web segura integrada ao Identity Management.
- Visualização de dados e gráficos provenientes exclusivamente do backend.
- Parametrização de ativos via interface gráfica.

### Dependências
- EP-5 (Core Calculation).
- EP-6 (Advanced Analytics).

### KPIs da Fase
- 100% das consultas refletindo dados oficiais do backend.
- Interface estável e responsiva para tomadores de decisão.

---

## EP-8. — Governance & Scale  
**Ref. BR-4.4 — Governança e Auditoria Avançada  
Ref. BR-4.5.2 — APIs Institucionais**

*(Auditoria formal, evidência institucional e escala)*

### Alinhamento com Business Requirements
Este EP evidencia formalmente os requisitos definidos em:

- **BR-4.4.1** Versionamento formal de parâmetros  
- **BR-4.4.2** Snapshot da base de dados utilizada  
- **BR-4.4.3** Histórico completo de execuções  
- **BR-4.4.4** Trilhas de auditoria completas  
- **BR-4.5.2** APIs institucionais (consulta)

> Esta fase **não cria nem altera cálculos, regras ou dados**.  
> Atua exclusivamente como camada de evidência, auditoria e conformidade.

### Objetivo
Evidenciar formalmente, para auditoria interna e externa, que os cálculos,
execuções e decisões já realizados possuem governança, rastreabilidade
e reprodutibilidade institucional.

### Escopo
- Consolidação documental da governança existente:
  - parâmetros utilizados
  - métodos e fórmulas aprovados
  - versões de código e serviços
- Apresentação de snapshots já produzidos da base efetivamente utilizada.
- Consolidação das trilhas de auditoria existentes:
  - quem executou
  - quando executou
  - o quê foi executado
  - com qual versão
- Relatórios formais de auditoria e conformidade.
- APIs institucionais de consulta (read-only).
- Políticas de retenção, compressão e cold storage sobre dados existentes.

### Dependências
- EP-5 (Core Calculation sob governança).
- EP-7 (Front-End Visual Web), quando aplicável.

### KPIs da Fase
- Evidência completa, íntegra e reproduzível apresentada ao auditor sem lacunas.
- Relatórios de auditoria aceitos sem ressalvas técnicas.
- Consultas institucionais operando dentro do SLA definido.


---

## EP-9. Observações Finais

- A governança é tratada como **fundação e eixo contínuo**, não como etapa tardia.
- O `Execution Identity` é o fio condutor de todas as fases, garantindo legitimidade, rastreabilidade e soberania técnica.
