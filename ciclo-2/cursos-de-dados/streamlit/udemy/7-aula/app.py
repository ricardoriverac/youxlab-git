import streamlit as st
import pandas as pd
import time 

st.set_page_config("Curso StreamLit", "👋","wide")

st.title("Bem Vindo a mais uma Aula de Streamlit")

# Barra de Progressão
# texto = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     bar.progress(i+1)
#     texto.text(f"Carregando... {i+1}%")
#     time.sleep(2)

def carregar(file):
    df = pd.read_csv(file)
    n_linhas, n_colunas = df.shape
    st.write(f"Esta planilha contém {n_linhas} linhas e {n_colunas} colunas")
    return df

st.subheader("Carregue aqui seu arquivo CSV")
file = st.file_uploader("Coloque seu arquivo aqui", type="csv")

if file:
    with st.spinner("Aguarde..."):
        df = carregar(file)
    st.write(df)