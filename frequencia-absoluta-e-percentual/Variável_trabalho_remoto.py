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

# Traduzir as respotas da coluna Trabalho Híbrido
def traduzir_Trabalho_Hibrido(tipo_de_trabalho):
    traducoes = {
        "Yes": "Sim",
        "No": "Não",
        "Hybrid": "Híbrido"
    }
    return traducoes.get(tipo_de_trabalho, tipo_de_trabalho)

df['Trabalho_Remoto'] = df['Trabalho_Remoto'].apply(traduzir_Trabalho_Hibrido)


# Calcular a frequência de trabalho remoto (coluna "Trabalho_Remoto")
# Contar as ocorrências de "SIM", "NÃO" e "HÍBRIDO"
frequencia_trabalho_remoto = df['Trabalho_Remoto'].value_counts()

# Calcular a frequência percentual
total_elementos = len(df['Trabalho_Remoto'])
frequencia_percentual = (frequencia_trabalho_remoto / total_elementos) * 100

# Criar DataFrame da tabela de frequências e percentuais
tabela_frequencias_trabalho_remoto = pd.DataFrame({
    'Categoria': frequencia_trabalho_remoto.index,
    'Frequência Absoluta': frequencia_trabalho_remoto.values,
    'Frequência Percentual': frequencia_percentual.values
})

# Exibir as estatísticas para Trabalho Remoto
print(f'\nTabela da variável TRABALHO REMOTO')
print(tabela_frequencias_trabalho_remoto)

# Gráfico de barras para visualizar a frequência dos departamentos
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(tabela_frequencias_trabalho_remoto['Categoria'], tabela_frequencias_trabalho_remoto['Frequência Absoluta'], color='skyblue')
ax.set_xlabel('Categoria')
ax.set_ylabel('Frequência Absoluta')
ax.set_title('Frequência Absoluta Trabalho Remoto')
ax.set_xticklabels(tabela_frequencias_trabalho_remoto['Categoria'], rotation=45, ha='right')
plt.tight_layout()

# Exibir o gráfico no Streamlit
st.pyplot(fig)


##streamlit run c:/Users/dudac/Desktop/Trabalho_Estatistica/Variável_trabalho_remoto.py [ARGUMENTS]
##rodar no terminal para exibir o código

