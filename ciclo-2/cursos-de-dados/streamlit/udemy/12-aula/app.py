import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")

st.title("Página de Dashboard da Empresa XPTO")

# Gráfico de Dispersão
data = pd.DataFrame({
    "X": np.random.randn(100),
    "Y": np.random.randn(100)
})

st.subheader("gráfico de Dispersão")
sns.scatterplot(x="X", y="Y", data=data)
st.pyplot()

# Gráfico de Histograma

data = np.random.randn(1000)
st.subheader("Gráfico de Histograma")
plt.hist(data, bins=16, )
st.pyplot()

# Gráfico de Pizza

data = pd.DataFrame({
    "Categoria": ["A", "B", "C", "D"],
    "Valores": [25, 30, 15, 20]
})

st.title("Gráfico de Pizza")
plt.pie(data["Valores"], labels=data["Categoria"])
st.pyplot()