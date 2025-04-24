import pandas as pd
import numpy as np
import statistics as stats

# Carregar o dataset com caminho relativo
df = pd.read_csv(r'../Analises_dataset-medidas-centrais/dataset.csv')

# Calcular a média
media_tasks_completed = df['Tasks_Completed_Per_Day'].mean()

# Calcular a moda
moda_tasks_completed = df['Tasks_Completed_Per_Day'].mode().iloc[0]

# Calcular a mediana
mediana_tasks_completed = df['Tasks_Completed_Per_Day'].median()

# Calcular os quartis (1º, 2º (mediana), 3º)
quartis_tasks_completed = stats.quantiles(df['Tasks_Completed_Per_Day'], n=4)

# Calcular o percentil (exemplo, percentil 90)
percentil_90_tasks_completed = np.percentile(df['Tasks_Completed_Per_Day'], 90)

# Exibir os resultados
print(f'A média da variável Tasks_Completed_Per_Day é: {media_tasks_completed}')
print(f'A mediana da variável Tasks_Completed_Per_Day é: {mediana_tasks_completed}')
print(f'A moda da variável Tasks_Completed_Per_Day é: {moda_tasks_completed}')
print(f'Os quartis da variável Tasks_Completed_Per_Day são: Q1 = {quartis_tasks_completed[0]}, Q2 (Mediana) = {quartis_tasks_completed[1]}, Q3 = {quartis_tasks_completed[2]}')
print(f'O percentil 90 da variável Tasks_Completed_Per_Day é: {percentil_90_tasks_completed}')
