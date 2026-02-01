import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide", page_title="Gráfico com o Plotly")

st.title('Scartter Plot')

df = px.data.gapminder()

fig1 = px.scatter(df, x='gdpPercap', y='lifeExp', color='continent', size='pop',
                    log_x=True, size_max=60, facet_col='continent')
fig1.update_layout(plot_bgcolor='white',
                    title='PIB x Expectativa de Vida',
                    xaxis=dict(title='PIB'),
                    yaxis=dict(title='Expectatia de Vida'),
                    legend_title='Continentes',
                    legend_title_font_color='red'
                    )

st.plotly_chart(fig1)