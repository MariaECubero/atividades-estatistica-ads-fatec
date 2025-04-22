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

# Variável 'Pontuacao_Produtividade'
# Calcular a amplitude
amplitude_produtividade = df['Pontuacao_Produtividade'].max() - df['Pontuacao_Produtividade'].min()

# Definir o número fixo de intervalos (10)
numero_intervalos_produtividade = 10

# Definir o tamanho do intervalo (range) de cada classe
tamanho_intervalo_produtividade = np.ceil(amplitude_produtividade / numero_intervalos_produtividade)  # A amplitude dividida pelo número de intervalos

# Criar os bins para a tabela de frequências
bins_produtividade = np.arange(df['Pontuacao_Produtividade'].min(), df['Pontuacao_Produtividade'].max() + tamanho_intervalo_produtividade, tamanho_intervalo_produtividade)

# Criar a tabela de frequências
frequencia_produtividade, intervalo_classes_produtividade = np.histogram(df['Pontuacao_Produtividade'], bins=bins_produtividade)

# Criar DataFrame da tabela de frequências
tabela_frequencias_produtividade = pd.DataFrame({
    'Intervalo de Pontuação de Produtividade': [f'{int(intervalo_classes_produtividade[i])} - {int(intervalo_classes_produtividade[i+1])}' for i in range(len(intervalo_classes_produtividade) - 1)],
    'Frequência Absoluta': frequencia_produtividade
})

# Calcular a frequência percentual
total_elementos_produtividade = len(df['Pontuacao_Produtividade'])
tabela_frequencias_produtividade['Frequência Percentual'] = (tabela_frequencias_produtividade['Frequência Absoluta'] / total_elementos_produtividade) * 100

# Exibir as estatísticas para a Pontuação de Produtividade
print(f'\nTabela variável PONTUAÇÃO DE PRODUTIVIDADE')
print(f'**Amplitude**: {amplitude_produtividade}')
print(f'**Número de intervalos (fixo de 10)**: {numero_intervalos_produtividade}')
print(f'**Tamanho do intervalo**: {tamanho_intervalo_produtividade}')
print(tabela_frequencias_produtividade)

# Criar o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Plotar o gráfico de barras
ax.bar(tabela_frequencias_produtividade['Intervalo de Pontuação de Produtividade'], tabela_frequencias_produtividade['Frequência Absoluta'], color='skyblue', edgecolor='black')

# Ajustar labels e título
ax.set_xlabel('Intervalos de Pontuação de Produtividade')
ax.set_ylabel('Frequência Absoluta')
ax.set_title('Distribuição de Frequência da Pontuação de Produtividade')

# Rotacionar os rótulos do eixo X para melhor visualização
plt.xticks(rotation=45, ha='right')

# Exibir o gráfico no Streamlit
st.pyplot(fig)
