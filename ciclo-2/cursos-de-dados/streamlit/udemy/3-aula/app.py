import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Aula 3",
    page_icon="👋",
)

st.write("# Bem vindo a Aula 3 👋")
st.write("## Aula 3 gravada dia 19")

caminho_arquivo_1 = 'xlsx/dados_teste.xlsx'
caminho_arquivo_2 = 'xlsx/planilha_vendas.xlsx'
df1 = pd.read_excel(caminho_arquivo_1)
df2 = pd.read_excel(caminho_arquivo_2)

st.dataframe(df1)
st.write("Uma outra forma")
st.table(df1)
st.write("Uma terceira forma")
st.write(df1)

st.write("Outro DataFrame")
st.dataframe(df2)