import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # Certifique-se de importar o matplotlib
import streamlit as st  # Certifique-se de importar o Streamlit

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

# Variável 'Salario_Anual'
# Calcular a amplitude
amplitude_salario = df['Salario_Anual'].max() - df['Salario_Anual'].min()

# Definir o número fixo de intervalos (10)
numero_intervalos = 10

# Definir o tamanho do intervalo (range) de cada classe
tamanho_intervalo_salario = np.ceil(amplitude_salario / numero_intervalos)  # A amplitude dividida pelo número de intervalos

# Criar os bins para a tabela de frequências
bins_salario = np.arange(df['Salario_Anual'].min(), df['Salario_Anual'].max() + tamanho_intervalo_salario, tamanho_intervalo_salario)

# Criar a tabela de frequências
frequencia_salario, intervalo_classes_salario = np.histogram(df['Salario_Anual'], bins=bins_salario)

# Criar DataFrame da tabela de frequências
tabela_frequencias_salario = pd.DataFrame({
    'Intervalo de Salário Anual': [f'{int(intervalo_classes_salario[i])} - {int(intervalo_classes_salario[i+1])}' for i in range(len(intervalo_classes_salario) - 1)],
    'Frequência Absoluta': frequencia_salario
})

# Calcular a frequência percentual
total_elementos_salario = len(df['Salario_Anual'])
tabela_frequencias_salario['Frequência Percentual'] = (tabela_frequencias_salario['Frequência Absoluta'] / total_elementos_salario) * 100

# Exibir as estatísticas para o Salário Anual
print(f'\nTabela variável SALÁRIO ANUAL')
print(f'**Amplitude**: {amplitude_salario}')
print(f'**Número de intervalos (fixo de 10)**: {numero_intervalos}')
print(f'**Tamanho do intervalo**: {tamanho_intervalo_salario}')
print(tabela_frequencias_salario)

# Criar o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Plotar o gráfico de barras
ax.bar(tabela_frequencias_salario['Intervalo de Salário Anual'], tabela_frequencias_salario['Frequência Absoluta'], color='skyblue', edgecolor='black')

# Ajustar labels e título
ax.set_xlabel('Intervalos de Salários')
ax.set_ylabel('Frequência Absoluta')
ax.set_title('Distribuição de Frequência de Salários')

# Rotacionar os rótulos do eixo X para melhor visualização
plt.xticks(rotation=45, ha='right')

# Exibir o gráfico no Streamlit
st.pyplot(fig)
