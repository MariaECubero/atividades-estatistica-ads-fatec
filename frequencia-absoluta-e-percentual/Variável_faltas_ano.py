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

# Coluna 'Faltas_Ano'
# Remover duplicatas e calcular o número de elementos únicos
n_unicos_faltas = len(df['Faltas_Ano'].drop_duplicates())

# Calcular a amplitude
amplitude_faltas = df['Faltas_Ano'].max() - df['Faltas_Ano'].min()

# Calcular o número de intervalos (raiz quadrada do número de elementos únicos)
intervalos_faltas = np.ceil(np.sqrt(n_unicos_faltas))  # raiz quadrada do número de elementos únicos

# Definir o tamanho do intervalo (range) de cada classe
tamanho_intervalo_faltas = np.ceil(amplitude_faltas / intervalos_faltas)  # A amplitude dividida pelo número de intervalos

# Criar a tabela de frequências
# Definir os limites inferiores e superiores das classes
bins_faltas = np.arange(df['Faltas_Ano'].min(), df['Faltas_Ano'].max() + tamanho_intervalo_faltas, tamanho_intervalo_faltas)

# Criar a tabela de frequências
frequencia_faltas, intervalo_classes_faltas = np.histogram(df['Faltas_Ano'], bins=bins_faltas)

# Ajuste para não repetir intervalos
intervalos_faltas_corrigidos = [f'{int(intervalo_classes_faltas[i])} - {int(intervalo_classes_faltas[i+1])}' for i in range(len(intervalo_classes_faltas) - 1)]

# Criar DataFrame da tabela de frequências
tabela_frequencias_faltas = pd.DataFrame({
    'Intervalo': intervalos_faltas_corrigidos,
    'Frequência Absoluta': frequencia_faltas
})

# Calcular a frequência percentual
total_elementos_faltas = len(df['Faltas_Ano'])
tabela_frequencias_faltas['Frequência Percentual'] = (tabela_frequencias_faltas['Frequência Absoluta'] / total_elementos_faltas) * 100

# Exibir as estatísticas
print(f'\nTabela da variável FALTAS ANO')
print(f'**Amplitude**: {amplitude_faltas}')
print(f'**Número de intervalos (raiz quadrada de elementos únicos)**: {intervalos_faltas}')
print(f'**Tamanho do intervalo**: {tamanho_intervalo_faltas}')
print(tabela_frequencias_faltas)

# Criar o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Plotar o gráfico de barras
ax.bar(tabela_frequencias_faltas['Intervalo'], tabela_frequencias_faltas['Frequência Absoluta'], color='skyblue', edgecolor='black')

# Ajustar labels e título
ax.set_xlabel('Intervalos de Faltas no Ano')
ax.set_ylabel('Frequência Absoluta')
ax.set_title('Distribuição de Frequência Faltas Ano')

# Rotacionar os rótulos do eixo X para melhor visualização
plt.xticks(rotation=45, ha='right')

# Exibir o gráfico no Streamlit
st.pyplot(fig)