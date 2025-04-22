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

# Calcular a frequência de cada tempo de empresa (aqui vamos tratar o tempo em anos)
# Como o 'Tempo_de_Empresa' é um valor contínuo, podemos criar intervalos para contar as frequências

# Calcular a amplitude
amplitude = df['Tempo_de_Empresa'].max() - df['Tempo_de_Empresa'].min()

# Calcular o número de intervalos (raiz quadrada do número de elementos únicos)
n_unicos = len(df['Tempo_de_Empresa'].drop_duplicates())
intervalos = np.ceil(np.sqrt(n_unicos))  # raiz quadrada do número de elementos únicos

# Definir o tamanho do intervalo (range) de cada classe
tamanho_intervalo = np.ceil(amplitude / intervalos)  # A amplitude dividida pelo número de intervalos

# Criar os bins para a tabela de frequências
bins = np.arange(df['Tempo_de_Empresa'].min(), df['Tempo_de_Empresa'].max() + tamanho_intervalo, tamanho_intervalo)

# Criar a tabela de frequências
frequencia, intervalo_classes = np.histogram(df['Tempo_de_Empresa'], bins=bins)

# Criar DataFrame da tabela de frequências
tabela_frequencias_tempo_empresa = pd.DataFrame({
    'Intervalo de Tempo de Empresa (anos)': [f'{int(intervalo_classes[i])} - {int(intervalo_classes[i+1])}' for i in range(len(intervalo_classes) - 1)],
    'Frequência Absoluta': frequencia
})

# Calcular a frequência percentual
total_elementos = len(df['Tempo_de_Empresa'])
tabela_frequencias_tempo_empresa['Frequência Percentual'] = (tabela_frequencias_tempo_empresa['Frequência Absoluta'] / total_elementos) * 100

# Exibir as estatísticas para o Tempo de Empresa
print(f'\nTabela variável TEMPO DE EMPRESA')
print(f'**Amplitude**: {amplitude}')
print(f'**Número de intervalos (raiz quadrada de elementos únicos)**: {intervalos}')
print(f'**Tamanho do intervalo**: {tamanho_intervalo}')
print(tabela_frequencias_tempo_empresa)

# Gráfico de barras para visualizar a frequência dos tempos de empresa
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(tabela_frequencias_tempo_empresa['Intervalo de Tempo de Empresa (anos)'], 
       tabela_frequencias_tempo_empresa['Frequência Absoluta'], color='skyblue')

ax.set_xlabel('Tempo de Empresa')
ax.set_ylabel('Frequência Absoluta')
ax.set_title('Frequência Absoluta por Tempo de Empresa')
ax.set_xticklabels(tabela_frequencias_tempo_empresa['Intervalo de Tempo de Empresa (anos)'], 
                   rotation=45, ha='right')

plt.tight_layout()

# Exibir o gráfico no Streamlit
st.pyplot(fig)


##rodar código no terminal:
## '     streamlit run c:/Users/dudac/Desktop/Trabalho_Estatistica/Variável_tempo_de_empresa.py [ARGUMENTS]  '