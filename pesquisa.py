import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Nome do arquivo de armazenamento
data_file = "farmap_survey_data.csv"

# Criar arquivo CSV se não existir
if not os.path.exists(data_file):
    df = pd.DataFrame(columns=["Pergunta", "Resposta"])
    df.to_csv(data_file, index=False)

# Função para salvar resposta
def salvar_resposta(pergunta, resposta):
    df = pd.read_csv(data_file)
    df = pd.concat([df, pd.DataFrame({"Pergunta": [pergunta], "Resposta": [resposta]})], ignore_index=True)
    df.to_csv(data_file, index=False)

# Título
title_html = "<h1 style='text-align: center; color: #4CAF50;'>Pesquisa de Satisfação - Farmap</h1>"
st.markdown(title_html, unsafe_allow_html=True)

# Perguntas e botões
perguntas = [
    "Você encontrou o que precisava?",
    "Gostou do nosso atendimento?",
    "Você voltaria ou indicaria a Farmap para um amigo ou familiar?"
]

respostas = {"Sim": 1, "Não": -1, "Talvez": 0}

for pergunta in perguntas:
    st.write(f"### {pergunta}")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("✅ Sim", key=f"sim_{pergunta}"):
            salvar_resposta(pergunta, respostas["Sim"])
    with col2:
        if st.button("❌ Não", key=f"nao_{pergunta}"):
            salvar_resposta(pergunta, respostas["Não"])
    with col3:
        if st.button("🤔 Talvez", key=f"talvez_{pergunta}"):
            salvar_resposta(pergunta, respostas["Talvez"])

# Carregar dados
if os.path.exists(data_file):
    df = pd.read_csv(data_file)
    contagem = df["Resposta"].value_counts().reindex([1, 0, -1], fill_value=0)
    
    # Criar gráfico de pizza
    fig = px.pie(
        names=["Sim", "Talvez", "Não"],
        values=contagem.values,
        title="Resultados da Pesquisa",
        color_discrete_map={"Sim": "#4CAF50", "Talvez": "#FFC107", "Não": "#F44336"}
    )
    st.plotly_chart(fig)
