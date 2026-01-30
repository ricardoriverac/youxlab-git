import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")

st.title("Página de Dashboard de Empresa XPTO")

st.subheader("Gráficos de Barras")

data = pd.DataFrame({
    "Cidade": ["João Pessoa", "Rio de Janeiro", "Conde", "Detroid"],
    "Vendas": [1000, 200, 150, 300]
})

st.bar_chart(data, x="Cidade", y="Vendas")

st.subheader("Gráficos de Linhas")

data = pd.DataFrame({
    "Dia": range(1, 31),
    "Vendas": np.random.randint(200, 1000, size=30)
})

st.line_chart(data, x="Dia", y="Vendas")