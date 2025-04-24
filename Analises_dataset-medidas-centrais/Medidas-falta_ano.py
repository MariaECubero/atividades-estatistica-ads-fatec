import pandas as pd
import numpy as np 
import statistics as stats

# Carregar o dataset com caminho relativo
df = pd.read_csv(r'../Analises_dataset-medidas-centrais/dataset.csv')

# Calcular a média
media_faltas = df['Absences_Per_Year'].mean()

# Calcular a moda
moda_faltas = df['Absences_Per_Year'].mode().iloc[0]

# Calcular a mediana
mediana_faltas = df['Absences_Per_Year'].median()

# Calcular os quartis (1º, 2º (mediana), 3º)
quartis = stats.quantiles(df['Absences_Per_Year'], n=4)

# Calcular o percentil (exemplo, percentil 90)
percentil_90 = np.percentile(df['Absences_Per_Year'], 90)

# Exibir os resultados
print(f'A média da variável faltas_ano é: {media_faltas}')
print(f'A mediana da variável faltas_ano é: {mediana_faltas}')
print(f'A moda da variável faltas_ano é: {moda_faltas}')
print(f'Os quartis da variável faltas_ano são: Q1 = {quartis[0]}, Q2 (Mediana) = {quartis[1]}, Q3 = {quartis[2]}')
print(f'O percentil 90 da variável faltas_ano é: {percentil_90}')