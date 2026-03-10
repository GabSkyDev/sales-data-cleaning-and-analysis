import pandas as pd

def data_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    print('Inicializando limpeza dos dados...')
    df_clean = df.copy()

    # Correção de 'Preco_Unitario'
    df_clean['Preco_Unitario'] = pd.to_numeric(df_clean['Preco_Unitario'], errors='coerce')
    # Correção de 'Cliente_ID'
    df_clean['Cliente_ID'] = pd.to_numeric(df_clean['Cliente_ID'], errors='coerce').astype('Int64')
    # Correção de 'Data_Compra' 
    df_clean['Data_Compra'] = pd.to_datetime(df_clean['Data_Compra'], errors='coerce')

    # Remoção/Substituição de valores ausentes (NaN)
    # Na tabela de quantidade, iremos preencher os valores ausentes com o valor da mediana, sendo mais robusta para outliers
    qtd_mediana = df_clean['Quantidade'].median()
    df_clean.fillna({'Quantidade': qtd_mediana}, inplace=True)
    # Na tabela 'Status_Entrega', iremos preencher os valores ausentes com a moda (mais frequente)
    moda_status_entrega = df_clean['Status_Entrega'].mode()[0]
    df_clean.fillna({'Status_Entrega': moda_status_entrega}, inplace=True)

    # Na tabela 'Cliente_ID' e 'Preco_Unitario', a melhor abordagem para tratar 
    # os valores ausentes é realizando a remoção, já que não é possível inferir esses dados
    df_clean.dropna(subset= ['Cliente_ID', 'Preco_Unitario'], inplace=True)

    # Remoção de duplicatas
    df_clean.drop_duplicates(inplace=True)

    # Remoção da valores em 'Quantidade' que estão muito distantes da média.
    # Uma abordagem comum é remover valores que estão além de 3 desvios padrão da média.
    limite_superior = df_clean['Quantidade'].mean() + 3 * df_clean['Quantidade'].std()
    df_clean = df_clean[df_clean['Quantidade'] < limite_superior]

    print("Dados limpos com sucesso!")

    return df_clean

