import streamlit as st
import plotly.express as px

df = px.data.gapminder().query("country == 'Canada'")

st.title('Gráficos com o Plotly')

fig1 = px.line(df, x='year', y='gdpPercap', title='PIB por Pessoa por Ano no Canadá', color_discrete_sequence=['red'], markers=True)
fig1.update_layout(xaxis_title='Ano', yaxis_title='PIB', font_color='red', font_family='Arial', title_font_family='Times New Roman', title_font_size=20)
st.plotly_chart(fig1)

df2 = px.data.gapminder()

fig2 = px.line(df2, x='year', y='gdpPercap',title="PIB por Pessoa por Ano no Mundo", facet_col='continent', line_group='country', color='country')

st.plotly_chart(fig2)