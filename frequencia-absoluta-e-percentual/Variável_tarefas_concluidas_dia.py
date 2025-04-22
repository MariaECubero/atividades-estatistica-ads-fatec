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

# Coluna 'Tarefas_Concluídas_Dia'
# Remover duplicatas e calcular o número de elementos únicos
n_unicos_tarefas = len(df['Tarefas_Concluídas_Dia'].drop_duplicates())

# Calcular a amplitude
amplitude_tarefas = df['Tarefas_Concluídas_Dia'].max() - df['Tarefas_Concluídas_Dia'].min()

# Calcular o número de intervalos (raiz quadrada do número de elementos únicos)
intervalos_tarefas = np.ceil(np.sqrt(n_unicos_tarefas))  # raiz quadrada do número de elementos únicos

# Definir o tamanho do intervalo (range) de cada classe
tamanho_intervalo_tarefas = np.ceil(amplitude_tarefas / intervalos_tarefas)  # A amplitude dividida pelo número de intervalos

# Criar a tabela de frequências
# Definir os limites inferiores e superiores das classes
bins_tarefas = np.arange(df['Tarefas_Concluídas_Dia'].min(), df['Tarefas_Concluídas_Dia'].max() + tamanho_intervalo_tarefas, tamanho_intervalo_tarefas)

# Criar a tabela de frequências
frequencia_tarefas, intervalo_classes_tarefas = np.histogram(df['Tarefas_Concluídas_Dia'], bins=bins_tarefas)

# Ajuste para não repetir intervalos
intervalos_tarefas_corrigidos = [f'{int(intervalo_classes_tarefas[i])} - {int(intervalo_classes_tarefas[i+1])}' for i in range(len(intervalo_classes_tarefas) - 1)]

# Criar DataFrame da tabela de frequências
tabela_frequencias_tarefas = pd.DataFrame({
    'Intervalo': intervalos_tarefas_corrigidos,
    'Frequência Absoluta': frequencia_tarefas
})

# Calcular a frequência percentual
total_elementos_tarefas = len(df['Tarefas_Concluídas_Dia'])
tabela_frequencias_tarefas['Frequência Percentual'] = (tabela_frequencias_tarefas['Frequência Absoluta'] / total_elementos_tarefas) * 100

# Exibir as estatísticas
print(f'\nTabela da variável TAREFAS CONCLUÍDAS POR DIA')
print(f'**Amplitude**: {amplitude_tarefas}')
print(f'**Número de intervalos (raiz quadrada de elementos únicos)**: {intervalos_tarefas}')
print(f'**Tamanho do intervalo**: {tamanho_intervalo_tarefas}')
print(tabela_frequencias_tarefas)

# Criar o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Plotar o gráfico de barras
ax.bar(tabela_frequencias_tarefas['Intervalo'], tabela_frequencias_tarefas['Frequência Absoluta'], color='skyblue', edgecolor='black')

# Ajustar labels e título
ax.set_xlabel('Intervalos Frequencia Tarefas Concluidas')
ax.set_ylabel('Frequência Absoluta')
ax.set_title('Distribuição de Tarefas Concluídas no dia')

# Rotacionar os rótulos do eixo X para melhor visualização
plt.xticks(rotation=45, ha='right')

# Exibir o gráfico no Streamlit
st.pyplot(fig)