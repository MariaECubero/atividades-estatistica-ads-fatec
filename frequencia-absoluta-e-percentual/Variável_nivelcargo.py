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

# Traduzir os níveis de trabalho
def traduzir_nivelcargo(nome_do_cargo):
    traducoes = {
        "Entry": "Iniciante",
        "Mid": "Pleno",
        "Senior": "Senior",
        "Manager": "Gerente"
    }
    return traducoes.get(nome_do_cargo, nome_do_cargo)

df['Nivel_Cargo'] = df['Nivel_Cargo'].apply(traduzir_nivelcargo)

# Calcular a frequência de cada nível de cargo
frequencia_nivel_cargo = df['Nivel_Cargo'].value_counts()

# Calcular a frequência percentual para cada nível de cargo
total_elementos = len(df['Nivel_Cargo'])
frequencia_percentual_nivel_cargo = (frequencia_nivel_cargo / total_elementos) * 100

# Criar DataFrame para a tabela de frequências
tabela_frequencias_nivel_cargo = pd.DataFrame({
    'Nivel de Cargo': frequencia_nivel_cargo.index,
    'Frequência Absoluta': frequencia_nivel_cargo.values,
    'Frequência Percentual': frequencia_percentual_nivel_cargo.values
})

# Exibir as estatísticas para o Nivel de Cargo
print(f'\nTabela da variável NÍVEL DE CARGO')
print(tabela_frequencias_nivel_cargo)

# Gráfico de barras para visualizar a frequência dos níveis de cargo
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(tabela_frequencias_nivel_cargo['Nivel de Cargo'], tabela_frequencias_nivel_cargo['Frequência Absoluta'], color='skyblue')
ax.set_xlabel('Nível de Cargo')
ax.set_ylabel('Frequência Absoluta')
ax.set_title('Frequência Absoluta por Nível de Cargo')
ax.set_xticklabels(tabela_frequencias_nivel_cargo['Nivel de Cargo'], rotation=45, ha='right')
plt.tight_layout()

# Exibir o gráfico no Streamlit
st.pyplot(fig)


## rodar esse código no terminal
##'  streamlit run c:/Users/dudac/Desktop/Trabalho_Estatistica/Variável_nivelcargo.py [ARGUMENTS]  '
