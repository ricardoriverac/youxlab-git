import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric("Vendas Mês Atual", value="10000", delta="3%")

# with col2:
#     st.metric("Vendas do Dia", value="500", delta="-30%")

# with col3:
#     st.metric("Despesas Menais", value="2000", delta="10%")

col1, col2, col3 = st.columns(3)

col1.metric("Ganhos", "5000", "-10%")
col2.metric("Despesas", "2000", "-10%")
lucro = (5000 - 2000)
col3.metric("Lucro", lucro, "-10%")

style_metric_cards()