import sys
import os

# Ajustar o caminho para importar módulos do src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pandas as pd
from src.visualization import (plot_revenue_by_category, plot_top_products_quantity, plot_daily_sales_trend, plot_delivery_status)
from src.processing import load_clean_and_process

# Carregar e processar os dados
df = load_clean_and_process('data/raw_data.csv')
df.to_csv('data/clean_data.csv', index=False)

# Gerar os relatórios visuais
plot_revenue_by_category(df, save_path='reports/figures/receita_categoria.png')
plot_top_products_quantity(df, save_path='reports/figures/produtos_quantidade.png')
plot_daily_sales_trend(df, save_path='reports/figures/vendas_diarias.png')
plot_delivery_status(df, save_path='reports/figures/status_entrega.png')

print("Relatórios gerados com sucesso!")