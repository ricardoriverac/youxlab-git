import streamlit as st
import pandas as pd

st.set_page_config(layout= "centered")

st.write("<h1><center>Usando SelectBox, MultiSelect, File Uploader e Slider</center></h1>", unsafe_allow_html=True)
st.subheader("Prof. Luciano Borba")

select = st.selectbox("Selecione uma cor: ", ("Vermelho", "Verde", "Azul"))
st.write(f"A cor selecionada é {select}")

multi = st.multiselect("Selecione as suas marcas de carros preferidas", ("BMW", "Nissan", "Toyota", "Mazda", "Honda"))
st.write(f"As marcas selecionadas foram: ")
for m in multi:
    st.write(m)

df = st.file_uploader("Selecione um arquivo excel", type="xlsx")

if df:
    data = pd.read_excel(df)
    st.dataframe(data)

image = st.file_uploader("Selecione um arquivo excel", type="png")

if image:
    st.image(image)