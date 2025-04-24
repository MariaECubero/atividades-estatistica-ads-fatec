import pandas as pd
import numpy as np
import statistics as stats

# Carregar o dataset com caminho relativo
df = pd.read_csv(r'../Analises_dataset-medidas-centrais/dataset.csv')
# Calcular a média
media_years_at_company = df['Years_at_Company'].mean()

# Calcular a moda
moda_years_at_company = df['Years_at_Company'].mode().iloc[0]

# Calcular a mediana
mediana_years_at_company = df['Years_at_Company'].median()

# Calcular os quartis (1º, 2º (mediana), 3º)
quartis_years_at_company = stats.quantiles(df['Years_at_Company'], n=4)

# Calcular o percentil (exemplo, percentil 90)
percentil_90_years_at_company = np.percentile(df['Years_at_Company'], 90)

# Exibir os resultados
print(f'A média da variável anos_na_empresa é: {media_years_at_company}')
print(f'A mediana da variável anos_na_empresa é: {mediana_years_at_company}')
print(f'A moda da variável anos_na_empresa é: {moda_years_at_company}')
print(f'Os quartis da variável anos_na_empresa são: Q1 = {quartis_years_at_company[0]}, Q2 (Mediana) = {quartis_years_at_company[1]}, Q3 = {quartis_years_at_company[2]}')
print(f'O percentil 90 da variável anos_na_empresa é: {percentil_90_years_at_company}')
