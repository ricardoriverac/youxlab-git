import streamlit as st

st.set_page_config(layout="wide")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.text_input("Coloque seu Nome: ")

with col2:
    st.text_input("Coloque seu Email: ")

with col3:
    st.number_input("Coloque sua Idade: ", step=1)

with col4:
    st.text_input("Coloque seu Cargo: ")

with col5:
    st.number_input("Coloque seu Salário: ")

st.text_area("Justifique por que devo lhe contratar: ")
st.button("Enviar")