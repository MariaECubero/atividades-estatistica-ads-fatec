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

# Coluna 'Reunioes_Semanais'
# Remover duplicatas e calcular o número de elementos únicos
n_unicos_reunioes = len(df['Reunioes_Semanais'].drop_duplicates())

# Calcular a amplitude
amplitude_reunioes = df['Reunioes_Semanais'].max() - df['Reunioes_Semanais'].min()

# Calcular o número de intervalos (raiz quadrada do número de elementos únicos)
intervalos_reunioes = np.ceil(np.sqrt(n_unicos_reunioes))  # raiz quadrada do número de elementos únicos

# Definir o tamanho do intervalo (range) de cada classe
tamanho_intervalo_reunioes = np.ceil(amplitude_reunioes / intervalos_reunioes)  # A amplitude dividida pelo número de intervalos

# Criar a tabela de frequências
# Definir os limites inferiores e superiores das classes
bins_reunioes = np.arange(df['Reunioes_Semanais'].min(), df['Reunioes_Semanais'].max() + tamanho_intervalo_reunioes, tamanho_intervalo_reunioes)

# Criar a tabela de frequências
frequencia_reunioes, intervalo_classes_reunioes = np.histogram(df['Reunioes_Semanais'], bins=bins_reunioes)

# Ajuste para não repetir intervalos
intervalos_reunioes_corrigidos = [f'{int(intervalo_classes_reunioes[i])} - {int(intervalo_classes_reunioes[i+1])}' for i in range(len(intervalo_classes_reunioes) - 1)]

# Criar DataFrame da tabela de frequências
tabela_frequencias_reunioes = pd.DataFrame({
    'Intervalo': intervalos_reunioes_corrigidos,
    'Frequência Absoluta': frequencia_reunioes
})

# Calcular a frequência percentual
total_elementos_reunioes = len(df['Reunioes_Semanais'])
tabela_frequencias_reunioes['Frequência Percentual'] = (tabela_frequencias_reunioes['Frequência Absoluta'] / total_elementos_reunioes) * 100

# Exibir as estatísticas
print(f'\nTabela da variável REUNIÕES SEMANAIS')
print(f'**Amplitude**: {amplitude_reunioes}')
print(f'**Número de intervalos (raiz quadrada de elementos únicos)**: {intervalos_reunioes}')
print(f'**Tamanho do intervalo**: {tamanho_intervalo_reunioes}')
print(tabela_frequencias_reunioes)

# Criar o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Plotar o gráfico de barras
ax.bar(tabela_frequencias_reunioes['Intervalo'], tabela_frequencias_reunioes['Frequência Absoluta'], color='skyblue', edgecolor='black')

# Ajustar labels e título
ax.set_xlabel('Intervalos de Reuniões')
ax.set_ylabel('Frequência Absoluta')
ax.set_title('Distribuição de Frequência Reuniões Semanais')

# Rotacionar os rótulos do eixo X para melhor visualização
plt.xticks(rotation=45, ha='right')

# Exibir o gráfico no Streamlit
st.pyplot(fig)
