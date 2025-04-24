import pandas as pd
import numpy as np
import statistics as stats

# Carregar o dataset com caminho relativo
df = pd.read_csv(r'../Analises_dataset-medidas-centrais/dataset.csv')

# Calcular a média
media_monthly_hours_worked = df['Monthly_Hours_Worked'].mean()

# Calcular a moda
moda_monthly_hours_worked = df['Monthly_Hours_Worked'].mode().iloc[0]

# Calcular a mediana
mediana_monthly_hours_worked = df['Monthly_Hours_Worked'].median()

# Calcular os quartis (1º, 2º (mediana), 3º)
quartis_monthly_hours_worked = stats.quantiles(df['Monthly_Hours_Worked'], n=4)

# Calcular o percentil (exemplo, percentil 90)
percentil_90_monthly_hours_worked = np.percentile(df['Monthly_Hours_Worked'], 90)

# Exibir os resultados
print(f'A média da variável horas_trabalhadas_por_mes é: {media_monthly_hours_worked}')
print(f'A mediana da variável horas_trabalhadas_por_mes é: {mediana_monthly_hours_worked}')
print(f'A moda da variável horas_trabalhadas_por_mes é: {moda_monthly_hours_worked}')
print(f'Os quartis da variável horas_trabalhadas_por_mes são: Q1 = {quartis_monthly_hours_worked[0]}, Q2 (Mediana) = {quartis_monthly_hours_worked[1]}, Q3 = {quartis_monthly_hours_worked[2]}')
print(f'O percentil 90 da variável horas_trabalhadas_por_mes é: {percentil_90_monthly_hours_worked}')
