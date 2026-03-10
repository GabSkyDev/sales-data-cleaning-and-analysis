import pandas as pd
import matplotlib.pyplot as plt
from src.data_cleaning import data_cleaning

def load_clean_and_process(path: str) -> pd.DataFrame:
    """Carrega, limpa e adiciona coluna Total_Venda."""
    df = pd.read_csv(path)
    df = data_cleaning(df)
    df = add_total_sale(df)
    return df

def add_total_sale(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['Total_Venda'] = df['Quantidade'] * df['Preco_Unitario']
    return df

def revenue_by_category(df: pd.DataFrame) -> pd.Series:
    receita_por_categoria = df.groupby('Categoria')['Total_Venda'].sum()
    return receita_por_categoria

def top_products_by_quantity(df: pd.DataFrame, n: int = 10)  -> pd.Series:
    produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).head(n)
    return produto_mais_vendido

def daily_sales(df: pd.DataFrame) -> pd.Series:
    df_temporal = df.set_index('Data_Compra')
    vendas_por_dia = df_temporal.resample('D')['Total_Venda'].sum()
    return vendas_por_dia