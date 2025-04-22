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

def traduzir_Trabalho(equilibrio_vida):
    traducoes = {
        "Poor": "Pobre",
        "Excellent": "Excelente",
        "Good": "Bom",
        "Average": "Média"
    }
    return traducoes.get(equilibrio_vida, equilibrio_vida)  # Retorna o próprio valor se não encontrar a tradução

# Aplicando a função à coluna
df['Equilibrio_Trabalho_Vida'] = df['Equilibrio_Trabalho_Vida'].apply(traduzir_Trabalho)

# Iniciando nova tabela para a variável "Equilibrio_Trabalho_Vida"
# Calcular a frequência de cada categoria de equilíbrio entre trabalho e vida
frequencia_equilibrio = df['Equilibrio_Trabalho_Vida'].value_counts()

# Calcular a frequência percentual para cada categoria
total_elementos = len(df['Equilibrio_Trabalho_Vida'])
frequencia_percentual_equilibrio = (frequencia_equilibrio / total_elementos) * 100

# Criar DataFrame para a tabela de frequências
tabela_frequencias_equilibrio = pd.DataFrame({
    'Equilibrio_Trabalho_Vida': frequencia_equilibrio.index,
    'Frequência Absoluta': frequencia_equilibrio.values,
    'Frequência Percentual': frequencia_percentual_equilibrio.values
})

# Exibir as estatísticas para a variável "Equilibrio_Trabalho_Vida"
print(f'\nTabela da variável EQUILÍBRIO ENTRE TRABALHO E VIDA')
print(tabela_frequencias_equilibrio)

# Gráfico de barras para visualizar a frequência de "Equilibrio_Trabalho_Vida"
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(tabela_frequencias_equilibrio['Equilibrio_Trabalho_Vida'], tabela_frequencias_equilibrio['Frequência Absoluta'], color='lightcoral')
ax.set_xlabel('Equilíbrio entre Trabalho e Vida')
ax.set_ylabel('Frequência Absoluta')
ax.set_title('Frequência Absoluta por Equilíbrio entre Trabalho e Vida')
ax.set_xticklabels(tabela_frequencias_equilibrio['Equilibrio_Trabalho_Vida'], rotation=45, ha='right')
plt.tight_layout()

# Exibir o gráfico no Streamlit
st.pyplot(fig)
