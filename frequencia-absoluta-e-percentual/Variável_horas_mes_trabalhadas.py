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

# Calcular a frequência de horas trabalhadas por mês
# Como o 'Horas_mes_Trabalhadas' é um valor contínuo, podemos criar intervalos para contar as frequências

# Calcular a amplitude
amplitude = df['Horas_mes_Trabalhadas'].max() - df['Horas_mes_Trabalhadas'].min()

# Calcular o número de intervalos (raiz quadrada do número de elementos únicos)
n_unicos = len(df['Horas_mes_Trabalhadas'].drop_duplicates())  # Número de elementos únicos na coluna
intervalos = np.ceil(np.sqrt(n_unicos))  # raiz quadrada do número de elementos únicos

# Definir o tamanho do intervalo (range) de cada classe
tamanho_intervalo = np.ceil(amplitude / intervalos)  # A amplitude dividida pelo número de intervalos

# Criar os bins para a tabela de frequências
bins = np.arange(df['Horas_mes_Trabalhadas'].min(), df['Horas_mes_Trabalhadas'].max() + tamanho_intervalo, tamanho_intervalo)

# Criar a tabela de frequências
frequencia, intervalo_classes = np.histogram(df['Horas_mes_Trabalhadas'], bins=bins)

# Criar DataFrame da tabela de frequências
tabela_frequencias_horas_trabalhadas = pd.DataFrame({
    'Intervalo de Horas Trabalhadas (meses)': [f'{int(intervalo_classes[i])} - {int(intervalo_classes[i+1])}' for i in range(len(intervalo_classes) - 1)],
    'Frequência Absoluta': frequencia
})

# Calcular a frequência percentual
total_elementos = len(df['Horas_mes_Trabalhadas'])
tabela_frequencias_horas_trabalhadas['Frequência Percentual'] = (tabela_frequencias_horas_trabalhadas['Frequência Absoluta'] / total_elementos) * 100

# Exibir as estatísticas para Horas Trabalhadas por Mês
print(f'\nTabela variável HORAS MÊS TRABALHADAS')
print(f'**Amplitude**: {amplitude}')
print(f'**Número de intervalos (raiz quadrada de elementos únicos)**: {intervalos}')
print(f'**Tamanho do intervalo**: {tamanho_intervalo}')
print(tabela_frequencias_horas_trabalhadas)

# Criar o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Plotar o gráfico de barras
ax.bar(tabela_frequencias_horas_trabalhadas['Intervalo de Horas Trabalhadas (meses)'], tabela_frequencias_horas_trabalhadas['Frequência Absoluta'], color='skyblue', edgecolor='black')

# Ajustar labels e título
ax.set_xlabel('Intervalos de Horas')
ax.set_ylabel('Frequência Absoluta')
ax.set_title('Distribuição Horas Mês Trabalhadas')

# Rotacionar os rótulos do eixo X para melhor visualização
plt.xticks(rotation=45, ha='right')

# Exibir o gráfico no Streamlit
st.pyplot(fig)