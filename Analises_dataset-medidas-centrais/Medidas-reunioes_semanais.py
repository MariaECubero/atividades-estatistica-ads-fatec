import pandas as pd
import numpy as np
import statistics as stats

# Carregar o dataset com caminho relativo
df = pd.read_csv(r'../Analises_dataset-medidas-centrais/dataset.csv')

# Calcular a média
media_meetings_per_week = df['Meetings_per_Week'].mean()

# Calcular a moda
moda_meetings_per_week = df['Meetings_per_Week'].mode().iloc[0]

# Calcular a mediana
mediana_meetings_per_week = df['Meetings_per_Week'].median()

# Calcular os quartis (1º, 2º (mediana), 3º)
quartis_meetings_per_week = stats.quantiles(df['Meetings_per_Week'], n=4)

# Calcular o percentil (exemplo, percentil 90)
percentil_90_meetings_per_week = np.percentile(df['Meetings_per_Week'], 90)

# Exibir os resultados
print(f'A média da variável reuniões_por_semana é: {media_meetings_per_week}')
print(f'A mediana da variável reuniões_por_semana é: {mediana_meetings_per_week}')
print(f'A moda da variável reuniões_por_semana é: {moda_meetings_per_week}')
print(f'Os quartis da variável reuniões_por_semana são: Q1 = {quartis_meetings_per_week[0]}, Q2 (Mediana) = {quartis_meetings_per_week[1]}, Q3 = {quartis_meetings_per_week[2]}')
print(f'O percentil 90 da variável reuniões_por_semana é: {percentil_90_meetings_per_week}')
