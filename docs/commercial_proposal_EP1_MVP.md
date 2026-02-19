# Proposta Comercial — EP-4 (MVP Foundation)

Framework Padronizado de Comparação de Ativos Financeiros

---
 
**Documento:** commercial_proposal_EP4_MVP.md  
**Natureza:** Comercial / Contratual  
**Audiência:** Diretoria, Compras, Jurídico  
**Versão:** 1.0  
**Status:** Aprovado  
**Elaboração:** PMO / Arquitetura / Produto  
**Validação:** Diretoria Executiva  

---

## 1. Sumário Executivo

Este documento formaliza a **proposta comercial da Fase EP-4 (MVP Foundation)** do Framework Padronizado de Comparação de Ativos Financeiros.

A EP-4 estabelece a **fundação técnica, institucional e auditável** do framework, sendo condição obrigatória para qualquer evolução funcional futura.

Embora esta proposta trate **contratualmente apenas da EP-4**, apresenta-se, para fins de governança e decisão estratégica, uma **expectativa de investimento para o projeto completo**, organizado por fases evolutivas.

---

## 2. Visão Geral do Projeto (Programa Completo)

O projeto foi concebido como um **programa faseado**, com gates formais de aprovação entre fases, reduzindo risco técnico, financeiro e regulatório.

### 2.1 Fases Evolutivas

| Fase | Denominação           | Objetivo                                             | Status Comercial               |
| ---- | --------------------- | ---------------------------------------------------- | ------------------------------ |
| EP-4 | MVP Foundation        | Fundação técnica, protocolo, identidade e governança | **Contratada neste documento** |
| EP-5 | Core Analytics        | Métricas estatísticas e financeiras base             | Expectativa                    |
| EP-6 | Advanced Risk         | Risco avançado, stress e cenários                    | Expectativa                    |
| EP-7 | Decision Layer        | Scores, ranking e apoio à decisão                    | Expectativa                    |
| EP-8 | Scaling & Integration | Performance, APIs e integrações                      | Expectativa                    |

---

## 3. Expectativa de Esforço Relativo — Visão Global (Referencial)

> **Nota Importante:** Os valores abaixo são **estimativas referenciais**, sem caráter contratual, sujeitas a revisão técnica e aprovação formal a cada fase.

| Fase | Escopo Resumido                  | Esforço      Relativo      |
| ---- | -------------------------------- | -------------------------- |
| EP-4 | Fundação técnica e institucional | 100% (base contratual)     |
| EP-5 | Cálculos financeiros base        | ~60–70% EP-4               |
| EP-6 | Risco avançado e stress          | ~70–80% EP-4               |
| EP-7 | Camada decisória                 | ~50–60% EP-4               |
| EP-8 | Escala e integrações             | ~40–50% EP-4               |

**Expectativa Total do Programa:** ~3,0x a 3,5x o investimento da EP-4

---

## 4. Escopo Contratado — EP-4 (MVP Foundation)

### 4.1 Objetivo da EP-4

Construir uma **base técnica inegociável**, garantindo que qualquer execução futura seja:

* Identificável  
* Rastreável  
* Governada  
* Auditável  
* Determinística  

Sem qualquer lógica de cálculo financeiro.

---

### 4.2 Funcionalidades Contratadas

Incluem, mas não se limitam a:

1. **Estrutura Modular do Backend**
   * Separação em camadas: application, domain, infrastructure

2. **Execution Protocol (Protocolo de Execução)**
   * Header Institucional  
   * Execution Context  
   * Governance Context  
   * Payload controlado  

3. **Dispatcher Institucional**
   * Bloqueio de bypass  
   * Orquestração centralizada  

4. **Identity Management**
   * Geração de Execution Identity única  
   * Hash criptográfico por execução  

5. **Governança de Métodos e Versões**
   * Registro de métodos autorizados  
   * Bloqueio preventivo de versões não homologadas  

6. **Auditoria Imutável (Append-only)**
   * Logs institucionais  
   * Abortagem automática em falha de auditoria  

7. **CLI Técnica de Inspeção**
   * Consulta por Execution Identity  
   * Inspeção completa de trilha de execução  

---

## 5. Itens Explicitamente Fora de Escopo (EP-4)

* Qualquer cálculo financeiro ou estatístico  
* Indicadores de risco (VaR, CVaR, Sharpe, etc.)  
* Rankings, scores ou recomendações  
* Interfaces gráficas para usuário final  
* Integrações com sistemas externos  

Esses itens pertencem a fases futuras e **não fazem parte desta contratação**.

---

## 6. Estimativa de Esforço — EP-4

### 6.1 Esforço por Perfil

| Perfil                    | Horas Estimadas |
| ------------------------- | --------------- |
| Arquiteto de Software     | 80              |
| Engenheiro Backend Sênior | 240             |
| Engenheiro Backend Pleno  | 200             |
| QA / Auditoria Técnica    | 120             |
| PMO / Gestão              | 80              |

**Total Estimado:** **720 horas**

---

### 6.2 Expectativa de Investimento — Visão Global

| Fase | Identificador | Nome                | Escopo / Objetivo Principal                                                                 | Investimento Estimado (R$) |
|----:|---------------|---------------------|----------------------------------------------------------------------------------------------|----------------------------|
| 1 | EP-4 | MVP Foundation | Fundação técnica, protocolo de execução, identidade e governança mínima institucional. | **155.000** |
| 2 | EP-5 | Core Calculation | Integração do serviço de cálculo com métricas básicas do MVP.                              | ~95.000 – 110.000 |
| 3 | EP-6 | Advanced Analytics | Métricas avançadas, VaR, CVaR, score e ranking.                                           | ~110.000 – 125.000 |
| 4 | EP-7 | Visual Delivery | Interface web institucional para consumo do MVP.                                         | ~75.000 – 95.000 |
| 5 | EP-8 | Governance & Scale | Governança formal, rastreabilidade, auditoria externa e escala.                          | ~60.000 – 75.000 |

**Expectativa total do programa:** aproximadamente R$ 465.000 a R$ 540.000

> Valores referenciais e não contratuais.  
> Cada fase depende de aprovação formal e entrega validada da fase anterior.


---
## 7. Cronograma Estimado

| Marco                  | Prazo    |
| ---------------------- | -------- |
| Kickoff                | Semana 0 |
| Fundação Arquitetural  | Semana 2 |
| Protocolo e Identidade | Semana 4 |
| Governança e Auditoria | Semana 6 |
| Testes Fase 1          | Semana 7 |
| Gate de Aceite    | Semana 8 |

---

## 8. Critérios de Aceite (Gate)

A EP-4 será considerada concluída quando:

* 100% dos testes da Fase 1 forem aprovados  
* Toda execução possuir Execution Identity válida  
* Não houver bypass de protocolo  
* Logs forem imutáveis e completos  
* Nenhuma lógica financeira estiver presente  

---

## 9. Condições de Continuidade

* A contratação da EP-4 **não implica** contratação automática das fases seguintes  
* Cada nova fase exigirá:
  * Proposta comercial própria  
  * Aprovação orçamentária  
  * Gate técnico de saída da fase anterior  

---

## 10. Validade da Proposta

Esta proposta é válida por **30 dias** a partir da data de apresentação.

---

## 11. Aprovação

| Nome | Cargo               | Assinatura | Data |
| ---- | ------------------- | ---------- | ---- |
|      | Diretoria Executiva |            |      |
|      | PMO                 |            |      |
|      | Jurídico            |            |      |
