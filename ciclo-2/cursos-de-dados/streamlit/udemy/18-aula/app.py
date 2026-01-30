import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

with st.popover('Exemplo WHITE'):
    st.write("Hello, Wolrd!")

with st.popover('Imagem de Gato de Internet'):
    st.image('gatinho-meme.jpeg')

with st.popover('Exemplo de Gráfico'):
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Criando o gráfico
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Seno")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Gráfico de Seno')
    ax.legend()

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)