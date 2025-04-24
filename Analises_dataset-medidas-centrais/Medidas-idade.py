import pandas as pd
import numpy as np
import statistics as stats

# Carregar o dataset com caminho relativo
df = pd.read_csv(r'../Analises_dataset-medidas-centrais/dataset.csv')

# Calcular a média
media_age = df['Age'].mean()

# Calcular a moda
moda_age = df['Age'].mode().iloc[0]

# Calcular a mediana
mediana_age = df['Age'].median()

# Calcular os quartis (1º, 2º (mediana), 3º)
quartis_age = stats.quantiles(df['Age'], n=4)

# Calcular o percentil (exemplo, percentil 90)
percentil_90_age = np.percentile(df['Age'], 90)

# Exibir os resultados
print(f'A média da variável idade é: {media_age}')
print(f'A mediana da variável idade é: {mediana_age}')
print(f'A moda da variável idade é: {moda_age}')
print(f'Os quartis da variável idade são: Q1 = {quartis_age[0]}, Q2 (Mediana) = {quartis_age[1]}, Q3 = {quartis_age[2]}')
print(f'O percentil 90 da variável idade é: {percentil_90_age}')
