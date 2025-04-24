import pandas as pd
import numpy as np
import statistics as stats

# Carregar o dataset com caminho relativo
df = pd.read_csv(r'../Analises_dataset-medidas-centrais/dataset.csv')

# Calcular a média
media_productivity_score = df['Productivity_Score'].mean()

# Calcular a moda
moda_productivity_score = df['Productivity_Score'].mode().iloc[0]

# Calcular a mediana
mediana_productivity_score = df['Productivity_Score'].median()

# Calcular os quartis (1º, 2º (mediana), 3º)
quartis_productivity_score = stats.quantiles(df['Productivity_Score'], n=4)

# Calcular o percentil (exemplo, percentil 90)
percentil_90_productivity_score = np.percentile(df['Productivity_Score'], 90)

# Exibir os resultados
print(f'A média da variável Productivity_Score é: {media_productivity_score}')
print(f'A mediana da variável Productivity_Score é: {mediana_productivity_score}')
print(f'A moda da variável Productivity_Score é: {moda_productivity_score}')
print(f'Os quartis da variável Productivity_Score são: Q1 = {quartis_productivity_score[0]}, Q2 (Mediana) = {quartis_productivity_score[1]}, Q3 = {quartis_productivity_score[2]}')
print(f'O percentil 90 da variável Productivity_Score é: {percentil_90_productivity_score}')
