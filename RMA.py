import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit import title

# Comando para configurar o layout da pagina
st.set_page_config(layout="wide")

df = pd.read_csv('RMA.CSV', delimiter=';', encoding = "ISO-8859-1")

df["DATA"] = pd.to_datetime(df["DATA"])
df = df.sort_values("DATA")

#verificando quandos meses tem no DataFrame
df["MES"] = df["DATA"].apply(lambda x: str(x.month) + "-" + str(x.year))

#A variavel mes sera inserido na Siderbar
mes = st.sidebar.selectbox("Mês", df["MES"].unique())

#filtra o mes
df_filtro = df[df["MES"] == mes]

#criar colunas no Dashboard
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

fig_data = px.bar(df_filtro, x = "DATA", y = "QUANTIDADE", color = "FORNECEDOR", title = "FORNECEDORES QUE FORAM MAIS ACIONADAS")
col1.plotly_chart(fig_data)

fig_prod = px.bar(df_filtro, x = "QUANTIDADE", y = "PRODUTO", color = "FORNECEDOR", title="PRODUTOS QUE MAIS VOLTARAM")
col2.plotly_chart(fig_prod)

loja_total = df_filtro.groupby("QUANTIDADE")[["PRODUTO"]].sum().reset_index()
fig_loja = px.bar(loja_total, x = "PRODUTO", y = "QUANTIDADE", title="QUANTIDADE DE PEÇAS ")
col3.plotly_chart(fig_loja)

fig_citu = px.pie(df_filtro, values = "QUANTIDADE", names="SITUAÇÃO", title = "SITUAÇÃO RMA")
col4.plotly_chart(fig_citu)