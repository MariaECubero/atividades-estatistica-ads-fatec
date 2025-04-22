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

# Traduzir os departamentos
def traduzir_departamento(nome_do_departamento):
    traducoes = {
        "Sales": "Vendas",
        "IT": "Tecnologia",
        "HR": "Recursos Humanos",
        "Finance": "Financeiro",
        "Marketing": "Publicidade",
        "Operations": "Operação"
    }
    return traducoes.get(nome_do_departamento, nome_do_departamento)

df['Departamento'] = df['Departamento'].apply(traduzir_departamento)

#Iniciando nova tabela da coluna "Departamentos"
# Calcular a frequência de cada departamento
frequencia_departamentos = df['Departamento'].value_counts()

# Calcular a frequência percentual para cada departamento
total_elementos = len(df['Departamento'])
frequencia_percentual = (frequencia_departamentos / total_elementos) * 100

# Criar DataFrame para a tabela de frequências
tabela_frequencias_departamentos = pd.DataFrame({
    'Departamento': frequencia_departamentos.index,
    'Frequência Absoluta': frequencia_departamentos.values,
    'Frequência Percentual': frequencia_percentual.values
})

# Exibir as estatísticas para o Departamento
print(f'\nTabela da variável DEPARTAMENTO')
print(tabela_frequencias_departamentos)


# Gráfico de barras para visualizar a frequência dos departamentos
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(tabela_frequencias_departamentos['Departamento'], tabela_frequencias_departamentos['Frequência Absoluta'], color='skyblue')
ax.set_xlabel('Departamento')
ax.set_ylabel('Frequência Absoluta')
ax.set_title('Frequência Absoluta por Departamento')
ax.set_xticklabels(tabela_frequencias_departamentos['Departamento'], rotation=45, ha='right')
plt.tight_layout()

# Exibir o gráfico no Streamlit
st.pyplot(fig)


## '   streamlit run c:/Users/dudac/Desktop/Trabalho_Estatistica/Variável_departamento.py [ARGUMENTS]  '
## rodar esse código no terminal