import streamlit as st
import pandas as pd
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

# Configurar layout responsivo
st.set_page_config(layout="wide")

# Título
title_html = """
    <div style='text-align: center;'>
        <h1 style='color: #4CAF50;'>Pesquisa de Satisfação - Farmap</h1>
    </div>
"""
st.markdown(title_html, unsafe_allow_html=True)

# Perguntas e botões
perguntas = [
    "Você encontrou o que precisava?",
    "Gostou do nosso atendimento?",
    "Você voltaria ou indicaria a Farmap para um amigo ou familiar?"
]

respostas = {"Sim": 1, "Não": -1, "Talvez": 0}

for pergunta in perguntas:
    st.markdown(f"<h3 style='text-align: center;'>{pergunta}</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("✅ Sim", key=f"sim_{pergunta}"):
            salvar_resposta(pergunta, respostas["Sim"])
    with col2:
        if st.button("❌ Não", key=f"nao_{pergunta}"):
            salvar_resposta(pergunta, respostas["Não"])
    with col3:
        if st.button("🤔 Talvez", key=f"talvez_{pergunta}"):
            salvar_resposta(pergunta, respostas["Talvez"])

# Mensagem de confirmação
st.markdown("""
    <div style='text-align: center; margin-top: 20px;'>
        <h3 style='color: #4CAF50;'>Obrigado por participar da nossa pesquisa!</h3>
    </div>
""", unsafe_allow_html=True)
