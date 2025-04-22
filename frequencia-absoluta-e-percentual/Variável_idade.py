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

# Supondo que o DataFrame seja chamado df e a coluna 'Idade' exista
# Remover duplicatas e calcular o número de elementos únicos
n_unicos = len(df['Idade'].drop_duplicates())

# Calcular a amplitude
amplitude = df['Idade'].max() - df['Idade'].min()

# Calcular o número de intervalos (raiz quadrada do número de elementos únicos)
intervalos = np.ceil(np.sqrt(n_unicos))  # raiz quadrada do número de elementos únicos

# Definir o tamanho do intervalo (range) de cada classe
tamanho_intervalo = np.ceil(amplitude / intervalos)  # A amplitude dividida pelo número de intervalos

# Criar a tabela de frequências
# Definir os limites inferiores e superiores das classes
bins = np.arange(df['Idade'].min(), df['Idade'].max() + tamanho_intervalo, tamanho_intervalo)

# Criar a tabela de frequências
frequencia, intervalo_classes = np.histogram(df['Idade'], bins=bins)

# Criar DataFrame da tabela de frequências
tabela_frequencias = pd.DataFrame({
    'Intervalo': [f'{int(intervalo_classes[i])} - {int(intervalo_classes[i+1])}' for i in range(len(intervalo_classes) - 1)],
    'Frequência Absoluta': frequencia
})

# Calcular a frequência percentual
total_elementos = len(df['Idade'])
tabela_frequencias['Frequência Percentual'] = (tabela_frequencias['Frequência Absoluta'] / total_elementos) * 100

# Exibir as estatísticas
print(f'\nTabela da variável IDADE')
print(f'**Amplitude**: {amplitude}')
print(f'**Número de intervalos (raiz quadrada de elementos únicos)**: {intervalos}')
print(f'**Tamanho do intervalo**: {tamanho_intervalo}')
print("\nTabela da variável IDADE")
print(tabela_frequencias)

# Criar o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Plotar o gráfico de barras
ax.bar(tabela_frequencias['Intervalo'], tabela_frequencias['Frequência Absoluta'], color='skyblue', edgecolor='black')

# Ajustar labels e título
ax.set_xlabel('Intervalos de Idade')
ax.set_ylabel('Frequência Absoluta')
ax.set_title('Distribuição de Frequência de Idade')

# Rotacionar os rótulos do eixo X para melhor visualização
plt.xticks(rotation=45, ha='right')

# Exibir o gráfico no Streamlit
st.pyplot(fig)

##rodar o script no terminal '  streamlit run c:/Users/dudac/Desktop/Trabalho_Estatistica/Variável_idade.py   '