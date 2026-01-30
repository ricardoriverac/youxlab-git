import streamlit as st

st.header("Aula 3 - Checkbox, Radio e Botões")
st.subheader("Com Luciano Borba")

banho = st.checkbox("Banho")
dentes = st.checkbox("Estudar os Dentes")

btn = st.button("Opinião")

if btn:
    # Checkbox
    if banho and dentes:
        st.success("Você está cheiroso(a) e com um ótimo hálito!")
    elif dentes is True and banho is False:
        st.warning("Você está com um ótimo hálito, mas precisa tomar um banho!")
    elif banho is True and dentes is False:
        st.warning("Você está cheiroso, mas precisa escovar os dentes!")
    else:
        st.warning("Você precisa tomar banho e escovar os dentes!")

# Radio
radio = st.radio("Qual a cor favorita do João?", options=["Vermelho", "Azul", "Verde", "Preto", "Branco"])

# Botões
responder = st.button("Responder")

if responder:
    if radio == "Vermelho":
        st.success(f"Você acertou!")
    else:
        st.warning("Você errou!")