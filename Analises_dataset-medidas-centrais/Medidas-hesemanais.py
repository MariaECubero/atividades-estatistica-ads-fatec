import pandas as pd
import numpy as np
import statistics as stats

# Carregar o dataset com caminho relativo
df = pd.read_csv(r'../Analises_dataset-medidas-centrais/dataset.csv')

# Calcular a média
media_overtime = df['Overtime_Hours_Per_Week'].mean()

# Calcular a moda
moda_overtime = df['Overtime_Hours_Per_Week'].mode().iloc[0]

# Calcular a mediana
mediana_overtime = df['Overtime_Hours_Per_Week'].median()

# Calcular os quartis (1º, 2º (mediana), 3º)
quartis_overtime = stats.quantiles(df['Overtime_Hours_Per_Week'], n=4)

# Calcular o percentil (exemplo, percentil 90)
percentil_90_overtime = np.percentile(df['Overtime_Hours_Per_Week'], 90)

# Exibir os resultados
print(f'A média da variável horas_extras_por_semana é: {media_overtime}')
print(f'A mediana da variável horas_extras_por_semana é: {mediana_overtime}')
print(f'A moda da variável horas_extras_por_semana é: {moda_overtime}')
print(f'Os quartis da variável horas_extras_por_semana são: Q1 = {quartis_overtime[0]}, Q2 (Mediana) = {quartis_overtime[1]}, Q3 = {quartis_overtime[2]}')
print(f'O percentil 90 da variável horas_extras_por_semana é: {percentil_90_overtime}')
