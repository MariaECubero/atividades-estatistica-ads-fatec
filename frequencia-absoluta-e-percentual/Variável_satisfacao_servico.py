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

# Coluna 'Satisfacao_Trabalho'
# Definir o número de intervalos
n_unicos_satisfacao = len(df['Satisfacao_Trabalho'].drop_duplicates())
amplitude_satisfacao = df['Satisfacao_Trabalho'].max() - df['Satisfacao_Trabalho'].min()
intervalos_satisfacao = np.ceil(np.sqrt(n_unicos_satisfacao))  # raiz quadrada do número de elementos únicos
tamanho_intervalo_satisfacao = np.ceil(amplitude_satisfacao / intervalos_satisfacao)

# Definir os limites dos intervalos
bins_satisfacao = np.arange(df['Satisfacao_Trabalho'].min(), df['Satisfacao_Trabalho'].max() + tamanho_intervalo_satisfacao, tamanho_intervalo_satisfacao)

# Criar a tabela de frequências
frequencia_satisfacao, intervalo_classes_satisfacao = np.histogram(df['Satisfacao_Trabalho'], bins=bins_satisfacao)

# Ajuste para não repetir intervalos
intervalos_satisfacao_corrigidos = [f'{int(intervalo_classes_satisfacao[i])} - {int(intervalo_classes_satisfacao[i+1])}' for i in range(len(intervalo_classes_satisfacao) - 1)]

# Criar DataFrame da tabela de frequências
tabela_frequencias_satisfacao = pd.DataFrame({
    'Intervalo': intervalos_satisfacao_corrigidos,
    'Frequência Absoluta': frequencia_satisfacao
})

# Calcular a frequência percentual
total_elementos_satisfacao = len(df['Satisfacao_Trabalho'])
tabela_frequencias_satisfacao['Frequência Percentual'] = (tabela_frequencias_satisfacao['Frequência Absoluta'] / total_elementos_satisfacao) * 100

# Exibir as estatísticas
print(f'\nTabela da variável SATISFAÇÃO NO TRABALHO')
print(f'**Amplitude**: {amplitude_satisfacao}')
print(f'**Número de intervalos (raiz quadrada de elementos únicos)**: {intervalos_satisfacao}')
print(f'**Tamanho do intervalo**: {tamanho_intervalo_satisfacao}')
print(tabela_frequencias_satisfacao)

# Criar o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Plotar o gráfico de barras
ax.bar(tabela_frequencias_satisfacao['Intervalo'], tabela_frequencias_satisfacao['Frequência Absoluta'], color='lightblue', edgecolor='black')

# Ajustar labels e título
ax.set_xlabel('Intervalos de Satisfação no Trabalho')
ax.set_ylabel('Frequência Absoluta')
ax.set_title('Distribuição de Frequência - Satisfação no Trabalho')

# Rotacionar os rótulos do eixo X para melhor visualização
plt.xticks(rotation=45, ha='right')

# Exibir o gráfico no Streamlit
st.pyplot(fig)

