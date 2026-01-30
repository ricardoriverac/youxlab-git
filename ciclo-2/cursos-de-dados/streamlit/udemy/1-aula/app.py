import streamlit as st

st.title("MinhaPágina - WSL")
st.header("Primeira Página")
st.subheader("Este é um subheader")
st.text("Posso estar adicionando um texto")
st.markdown("---")
st.markdown("> Aqui eu tenho uma citação")
st.markdown("**Negrito** e *Italiano*")
st.caption("Aqui eu tenho uma legenda")
st.latex("x=(283+14)/(2321-2)*2")
st.text("x=(283+14)/(2321-2)*2")
json = {
    "Nome": "João",
    "Idade": 25
}
st.json(json)
codigo = """
def funcao():
    retrun false
"""
st.code(codigo, language="python")