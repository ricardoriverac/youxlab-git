import streamlit as st
import pandas as pd


df = pd.read_csv("dados_validos.csv")

st.set_page_config(page_title="Dashboard de HR", page_icon=":bar_chart:", layout="wide")

st.title("Paineis de recursos Humanos")

idade = 