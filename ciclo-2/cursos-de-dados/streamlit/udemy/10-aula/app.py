import streamlit as st
from datetime import datetime


st.set_page_config("Opções de Input")

st.title("Opções de Input com Streamlit")

v1 = st.text_input("Coloque seu nome: ", max_chars=50)
v2 = st.text_area("Descreva quem você é: ", max_chars=500)
v3 = st.number_input("Coloque sua Idade: ", min_value=0, max_value=100)
v4 = st.date_input("Coloque sua data de nascimento: ", min_value="1900-01-01") # ou min_value=datetime(1900, 1, 1)
v5 = st.time_input("Indique a hora que deseja agendar: ")
v6 = st.slider("Selecione o valor entre 0 e 100: ", min_value=0, max_value=100, value=25)

if v1:
    st.write(f"Seu nome é {v1}")
    st.write(f"Se descreve da seguinte forma: {v2}")
    st.write(f"Sua idade é: {v3}")
    st.write(f"Sua data de nascimento é {v4}")