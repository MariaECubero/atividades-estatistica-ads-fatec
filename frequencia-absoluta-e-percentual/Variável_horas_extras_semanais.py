import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 

# Carregar o dataset
df = pd.read_csv(r'C:\Users\dudac\Desktop\Trabalho_Estatistica\dataset.csv')

# Renomear as colunas manualmente
df = df.rename(columns={
    'Employee_ID': 'ID_Funcionario',
    'Age': 'Idade',
    'Department' : 'Departamento',
    'Job_Level' : 'Nivel_Cargo',
    'Years_at_Company' : 'Tempo_de_Empresa',
    'Monthly_Hours_Worked' : 'Horas_mes_Trabalhadas',
    'Remote_Work' : 'Trabalho_Remoto',
    'Meetings_per_Week' : 'Reunioes_Semanais',
    'Tasks_Completed_Per_Day' : 'Tarefas_Concluídas_Dia',
    'Overtime_Hours_Per_Week' : 'Horas_Extras_Semanais',    
    'Annual_Salary' : 'Salario_Anual', 
    'Absences_Per_Year' : 'Faltas_Ano',
    'Work_Life_Balance' : 'Equilibrio_Trabalho_Vida', 
    'Job_Satisfaction' : 'Satisfacao_Trabalho', 
    'Productivity_Score' : 'Pontuacao_Produtividade' 
})

# Coluna 'Horas_Extras_Semanais'
# Remover duplicatas e calcular o número de elementos únicos
n_unicos_horas_extras = len(df['Horas_Extras_Semanais'].drop_duplicates())

# Calcular a amplitude
amplitude_horas_extras = df['Horas_Extras_Semanais'].max() - df['Horas_Extras_Semanais'].min()

# Calcular o número de intervalos (raiz quadrada do número de elementos únicos)
intervalos_horas_extras = np.ceil(np.sqrt(n_unicos_horas_extras))  # raiz quadrada do número de elementos únicos

# Definir o tamanho do intervalo (range) de cada classe
tamanho_intervalo_horas_extras = np.ceil(amplitude_horas_extras / intervalos_horas_extras)  # A amplitude dividida pelo número de intervalos

# Criar a tabela de frequências
# Definir os limites inferiores e superiores das classes
bins_horas_extras = np.arange(df['Horas_Extras_Semanais'].min(), df['Horas_Extras_Semanais'].max() + tamanho_intervalo_horas_extras, tamanho_intervalo_horas_extras)

# Criar a tabela de frequências
frequencia_horas_extras, intervalo_classes_horas_extras = np.histogram(df['Horas_Extras_Semanais'], bins=bins_horas_extras)

# Ajuste para não repetir intervalos
intervalos_horas_extras_corrigidos = [f'{int(intervalo_classes_horas_extras[i])} - {int(intervalo_classes_horas_extras[i+1])}' for i in range(len(intervalo_classes_horas_extras) - 1)]

# Criar DataFrame da tabela de frequências
tabela_frequencias_horas_extras = pd.DataFrame({
    'Intervalo': intervalos_horas_extras_corrigidos,
    'Frequência Absoluta': frequencia_horas_extras
})

# Calcular a frequência percentual
total_elementos_horas_extras = len(df['Horas_Extras_Semanais'])
tabela_frequencias_horas_extras['Frequência Percentual'] = (tabela_frequencias_horas_extras['Frequência Absoluta'] / total_elementos_horas_extras) * 100

# Exibir as estatísticas
print(f'\nTabela da variável HORAS EXTRAS SEMANAIS')
print(f'**Amplitude**: {amplitude_horas_extras}')
print(f'**Número de intervalos (raiz quadrada de elementos únicos)**: {intervalos_horas_extras}')
print(f'**Tamanho do intervalo**: {tamanho_intervalo_horas_extras}')
print(tabela_frequencias_horas_extras)

# Criar o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Plotar o gráfico de barras
ax.bar(tabela_frequencias_horas_extras['Intervalo'], tabela_frequencias_horas_extras['Frequência Absoluta'], color='skyblue', edgecolor='black')

# Ajustar labels e título
ax.set_xlabel('Intervalos de Horas Extras')
ax.set_ylabel('Frequência Absoluta')
ax.set_title('Distribuição de Frequência Horas Extras Semanais')

# Rotacionar os rótulos do eixo X para melhor visualização
plt.xticks(rotation=45, ha='right')

# Exibir o gráfico no Streamlit
st.pyplot(fig)