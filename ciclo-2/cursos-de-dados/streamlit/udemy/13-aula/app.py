import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.set_page_config(
        page_title="Gráfico Interrativos",
        page_icon="📈",
        layout="wide"
    )
    st.title("Gráfico Interrativos - Plotly e Streamlit")

    df = pd.read_csv("fiveyeardata.csv")

    st.write("## Dados Utilizados:")
    st.dataframe(df)

    st.subheader("Gráfico de Dispersão")
    fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country", log_x=True, size_max=60)
    st.plotly_chart(fig)

    st.subheader("Gráfico de Linhas")
    df_continent = df.groupby(["continent", "year"])["lifeExp"].mean().reset_index()
    fig = px.line(df_continent, x="year", y="lifeExp", color="continent", line_group="continent", title="Exprectativa de vida por ano e continente")
    st.plotly_chart(fig)

    st.subheader("Gráfico de Barras")
    fig = px.bar(df, x="year", y="pop", color="continent", title="População por Ano e continente")
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()