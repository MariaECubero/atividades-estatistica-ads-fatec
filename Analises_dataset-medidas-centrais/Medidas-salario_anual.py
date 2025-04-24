import pandas as pd
import numpy as np
import statistics as stats

# Carregar o dataset com caminho relativo
df = pd.read_csv(r'../Analises_dataset-medidas-centrais/dataset.csv')

# Calcular a média
media_annual_salary = df['Annual_Salary'].mean()

# Calcular a moda
moda_annual_salary = df['Annual_Salary'].mode().iloc[0]

# Calcular a mediana
mediana_annual_salary = df['Annual_Salary'].median()

# Calcular os quartis (1º, 2º (mediana), 3º)
quartis_annual_salary = stats.quantiles(df['Annual_Salary'], n=4)

# Calcular o percentil (exemplo, percentil 90)
percentil_90_annual_salary = np.percentile(df['Annual_Salary'], 90)

# Exibir os resultados
print(f'A média da variável Annual_Salary é: {media_annual_salary}')
print(f'A mediana da variável Annual_Salary é: {mediana_annual_salary}')
print(f'A moda da variável Annual_Salary é: {moda_annual_salary}')
print(f'Os quartis da variável Annual_Salary são: Q1 = {quartis_annual_salary[0]}, Q2 (Mediana) = {quartis_annual_salary[1]}, Q3 = {quartis_annual_salary[2]}')
print(f'O percentil 90 da variável Annual_Salary é: {percentil_90_annual_salary}')
