import pandas as pd
import matplotlib.pyplot as plt
from .processing import revenue_by_category, top_products_by_quantity, daily_sales 

def plot_revenue_by_category(df: pd.DataFrame, save_path: str = '../reports/figures'):
    """Plota receita total por categoria de produto."""
    receita_por_categoria = revenue_by_category(df)
    receita_por_categoria.plot(kind='bar', color='teal')
    plt.title('Receita Total Por Categoria de Produto')
    plt.ylabel('Receita (R$)')
    plt.xlabel('Categoria')
    plt.xticks(rotation=0)
    if save_path:
        plt.savefig(save_path)

def plot_top_products_quantity(df: pd.DataFrame, n: int = 10, save_path: str = '../reports/figures'):
    """Plota quantidade vendida por produto (top N)."""
    produto_mais_vendido = top_products_by_quantity(df, n)
    produto_mais_vendido.plot(kind='barh', color='mediumseagreen')
    plt.title('Quantidade de Unidades Vendidas por Produto')
    plt.ylabel('Produto')
    plt.xlabel('Quantidade Vendida')
    plt.gca().invert_yaxis()
    if save_path:
        plt.savefig(save_path)

def plot_daily_sales_trend(df: pd.DataFrame, save_path: str = '../reports/figures'):
    """Plota tendência de vendas diárias."""
    vendas_por_dia = daily_sales(df)
    vendas_por_dia.plot(kind='line', marker='.', linestyle='-', color='royalblue')
    plt.title('Tendência de Vendas Diárias')
    plt.ylabel('Receita (R$)')
    plt.xlabel('Data')
    if save_path:
        plt.savefig(save_path)

def plot_delivery_status(df: pd.DataFrame, save_path: str = '../reports/figures'):
    """Plota a distribuição dos status de entrega das vendas"""
    status_entrega_count = df['Status_Entrega'].value_counts()
    plt.pie(
        status_entrega_count,                 # Valores numéricos para cada fatia (quantidade de cada status)
        labels = status_entrega_count.index,  # Rótulos de cada fatia (labels dos status)
        autopct = '%1.1f%%',                  # Mostra o percentual em cada fatia com 1 casa decimal
        startangle = 180,                     # Ângulo inicial para "girar" o gráfico e escolher onde começa a primeira fatia
        colors = ['springgreen',              # Cor da primeira fatia
                'gold',                       # Cor da segunda fatia
                'crimson']                    # Cor da terceira fatia


    )
    plt.title('\nDistribuição do Status de Entrega')
    if save_path:
        plt.savefig(save_path)