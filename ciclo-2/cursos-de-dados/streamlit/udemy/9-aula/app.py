import streamlit as st

st.set_page_config(page_title="João Othávio", page_icon="sunglasses", layout="wide")
st.title("Curso Streamlit com João Othávio")

with st.expander("Sobre mim:"):
    st.write("Eu sou o João Othávio")
    st.write("Estudande de Dados & CyberSecurity")
st.divider()
with st.form("Formulário de Inscrição"):
    nome = st.text_input("Nome:")
    email = st.text_input("Email:")
    botao = st.form_submit_button("Enviar")

if botao:
    st.success(f"Ficha Incrita com sucesso, Nome: {nome}\nEmail: {email}")