import streamlit as st

st.title("Função `st.tabs`")
st.subheader("Com Luciano Borba")

tab1, tab2, tab3, tab4 = st.tabs(["Modelagem de Dados", "SQL", "Modelagem Dimenssional", "Python"])

with tab1:
    st.header("Modelagem de Dados")
    st.subheader("É importante de começar pela base!")

with tab2:
    st.header("SQL")
    st.subheader("É mais importante que python para área de dados!")

with tab3:
    st.header("Modelagem Dimenssional")
    st.subheader("Deveras importante para Construção de DW")

with tab4:
    st.header("Python")
    st.subheader("Python >>> Java")