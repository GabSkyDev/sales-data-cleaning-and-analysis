# 📊 Sales Data Cleaning and Analysis

Uma solução completa para limpeza, processamento e análise de dados de vendas, com geração de insights acionáveis e relatórios executivos.

---

## 📍 1. Visão Geral

Este projeto implementa um pipeline de dados robusto para análise de vendas, cobrindo desde a ingestão e limpeza de dados brutos até a geração de visualizações e relatórios executivos. A solução permite que gestores e stakeholders entendam rapidamente o desempenho do negócio através de métricas-chave e padrões identificados nos dados de vendas.

**Objetivo Principal:** Transformar dados brutos em insights estratégicos para suportar decisões de negócio fundamentadas em dados.

---

## 📝 2. Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)

---

## 📜 3. Instalação e Uso

### Pré-requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)
- Git (controle de versão)

### Instruções de Instalação

#### 1. Clone o repositório

```bash
git clone https://github.com/GabSkyDev/sales-data-cleaning-and-analysis.git
cd sales-data-cleaning-and-analysis
```

#### 2. Crie um ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### Uso do Projeto

#### Executar a análise completa

```bash
python main.py
```

#### Gerar relatórios

```bash
python -m scripts.generate_reports
```

#### Executar notebooks interativos

```bash
jupyter notebook notebooks/
```

Os notebooks estão organizados sequencialmente:
- `01_data_cleaning.ipynb` - Limpeza e preparação dos dados
- `02_data_processing.ipynb` - Engenharia de atributos e extração de insights
- `03_sales_insights.ipynb` - Visualizações e análise de negócio

---

## 🎯 4. Definição e Problema de Negócio

### Problema Identificado

Dados de vendas brutos frequentemente contêm inconsistências, valores ausentes, duplicatas e outliers que dificultam análises confiáveis. Sem um processamento adequado, gestores podem tomar decisões baseadas em informações imprecisas.

### Questões de Negócio Respondidas

1. **Qual é a receita total de vendas?**
   - Compreender o desempenho financeiro geral do período

2. **Qual categoria gera mais receita?**
   - Identificar segmentos de maior valor para alocação de recursos

3. **Quais produtos são mais vendidos?**
   - Compreender preferências dos clientes e volume de movimentação

4. **Como a venda varia ao longo do tempo?**
   - Identificar sazonalidade e padrões temporais para planejamento

5. **Qual é a qualidade do processo de entrega?**
   - Monitorar taxa de sucesso e identificar gargalos logísticos

### Solução Proposta

Um pipeline automatizado que:
- ✅ Limpa e valida os dados  
- ✅ Agrega métricas de negócio  
- ✅ Gera visualizações intuitivas  
- ✅ Produz relatórios executivos  

---

## 🗂️ 5. Estrutura de Pastas e Explicação de Soluções

```
sales-data-cleaning-and-analysis/
├── main.py                          # Script principal de execução
├── requirements.txt                 # Dependências do projeto
├── README.md                        # Este arquivo
│
├── data/                            # Armazenamento de dados
│   ├── raw_data.csv                # Dados brutos (origem)
│   └── clean_data.csv              # Dados processados e limpos
│
├── notebooks/                       # Análise exploratória interativa
│   ├── 01_data_cleaning.ipynb      # Etapa 1: Limpeza de dados
│   ├── 02_data_processing.ipynb    # Etapa 2: Feature engineering
│   └── 03_sales_insights.ipynb     # Etapa 3: Visualizações e insights
│
├── reports/                         # Saídas e documentação
│   ├── analysis_report.md          # Relatório executivo (análise final)
│   └── figures/                    # Gráficos e visualizações
│       ├── receita_categoria.png
│       ├── produtos_quantidade.png
│       ├── vendas_diarias.png
│       └── status_entrega.png
│
├── scripts/                         # Scripts de automação
│   └── generate_reports.py         # Geração automática de relatórios
│
└── src/                             # Módulos reutilizáveis
    ├── __init__.py
    ├── data_cleaning.py            # Funções de limpeza de dados
    ├── processing.py               # Funções de processamento e aggregação
    └── visualization.py            # Funções de visualização
```

### Descrição Detalhada

| Pasta/Arquivo | Propósito | Solução Implementada |
|---|---|---|
| `data/` | Armazenamento de dados | Separação entre dados brutos e processados |
| `notebooks/` | Exploração e análise | Scripts interativos para compreensão do pipeline |
| `reports/` | Saídas finais | Relatório executivo em Markdown + visualizações em PNG |
| `scripts/` | Automação | Geração automática de artefatos sem intervalo manual |
| `src/` | Lógica modular | Funções reutilizáveis para limpeza, processamento e visualização |

### Detalhes de Implementação

#### `src/data_cleaning.py`
Função `data_cleaning()` que realiza:
- Conversão de tipos de dados
- Tratamento de valores ausentes (mediana para Quantidade, moda para Status_Entrega)
- Remoção de duplicatas
- Tratamento de outliers (valores fora de 3 desvios padrão)

#### `src/processing.py`
Funções para agregação de dados:
- `load_clean_and_process()` - Pipeline completo de carga e limpeza
- `revenue_by_category()` - Agregação de receita por categoria
- `top_products_by_quantity()` - Produtos mais vendidos
- `daily_sales()` - Vendas por dia (análise temporal)

#### `src/visualization.py`
Funções para geração de gráficos (extensão futura):
- Gráficos de barras e linhas
- Gráficos de pizza
- Análises de tendências

---

## 📋 6. Conclusão

Este projeto demonstra uma abordagem profissional e sistemática para análise de dados de vendas, combinando boas práticas de engenharia de software com rigor analítico.

### Próximas Etapas

Para uma compreensão completa dos insights gerados e recomendações estratégicas, **consulte o [Relatório Executivo de Análise de Vendas](./reports/analysis_report.md)**.

O relatório contém:
- 📊 Principais métricas de negócio
- 📈 Análise de categorias e produtos
- 📉 Tendências temporais
- 💡 Recomendações estratégicas acionáveis

### Contribuições Futuras

Possíveis melhorias e extensões:
- Dashboards interativos (Power BI)

---
