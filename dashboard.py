from string import whitespace
from webbrowser import BackgroundBrowser
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Driver Engagement Dashboard",
    layout="wide"
)

df = pd.read_csv("outputs/drivers_com_engajamento.csv")


df["nivel_engajamento"] = pd.Categorical(
    df["nivel_engajamento"],
    categories=["Alto", "Médio", "Baixo"],
    ordered=True
)

st.markdown(
    """
    <h1 style='text-align: center;'>
        Driver Engagement Dashboard – 99
    </h1>
    <h2></h2>
    """,
    unsafe_allow_html=True
)


# KPIs

col2, col3, col4, col1 = st.columns(4)
col1.metric("Total de Motoristas", len(df))
col2.metric("Engajamento Alto", (df["nivel_engajamento"] == "Alto").sum())
col3.metric("Engajamento Médio", (df["nivel_engajamento"] == "Médio").sum())
col4.metric("Engajamento Baixo", (df["nivel_engajamento"] == "Baixo").sum())


# WARNING AUTOMÁTICO

if (df["nivel_engajamento"] == "Alto").sum() == 0:
    st.warning(
        " Nenhum motorista atingiu **alto nível de engajamento** no período analisado."
    )

st.divider()


# Cores por engajamento

cores = {
    "Alto": "#00fa68",
    "Médio": "#ffcc00",
    "Baixo": "#fa1900"
}


# Gráfico 1 – Distribuição

st.subheader(" Distribuição de Motoristas por Engajamento")

contagem = (
    df["nivel_engajamento"]
    .value_counts()
    .reindex(["Alto", "Médio", "Baixo"], fill_value=0)
)

fig1, ax1 = plt.subplots(figsize=(12, 6))
bars = ax1.bar(
    contagem.index,
    contagem.values,
    color=[cores[n] for n in contagem.index]
)

for bar in bars:
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        int(bar.get_height()),
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold"
    )

ax1.set_xlabel("Nível de Engajamento")
ax1.set_ylabel("Quantidade de Motoristas")

st.pyplot(fig1)

st.divider()


# Gráfico 2 – Corridas Semanais (Pizza)

st.subheader("Corridas Semanais por Engajamento")

corridas_por_engajamento = df.groupby("nivel_engajamento")["corridas_semana"].sum().reindex(["Alto", "Médio", "Baixo"], fill_value=0)

fig2, ax2 = plt.subplots(figsize=(8, 8))
ax2.pie(
    corridas_por_engajamento,
    labels=corridas_por_engajamento.index,
    autopct='%1.1f%%',
    colors=[cores[n] for n in corridas_por_engajamento.index],
    startangle=90,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1.5, 'linestyle': 'solid'}
)
ax2.set_title(" Corridas Semanais por Engajamento", fontsize=16, fontweight='bold')

st.pyplot(fig2)
st.divider()


# Gráfico 3 – Média de Corridas

st.subheader(" Média de Corridas Semanais")

media_corridas = df.groupby("nivel_engajamento")["corridas_semana"].mean()

fig3, ax3 = plt.subplots(figsize=(10, 5))
bars = ax3.bar(
    media_corridas.index,
    media_corridas.values,
    color=[cores[n] for n in media_corridas.index]
)

for bar in bars:
    ax3.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():.1f}",
        ha="center",
        va="bottom",
        fontsize=11,
        fontweight="bold"
    )

ax3.set_xlabel("Nível de Engajamento")
ax3.set_ylabel("Média de Corridas")

st.pyplot(fig3)

st.divider()


# Função para pintar o score

def color_score(val, df_subset):
    if val == df_subset["score_engajamento"].max():
        return 'color: green; font-weight: bold'
    elif val == df_subset["score_engajamento"].min():
        return 'color: red; font-weight: bold'
    else:
        return ''


# Top 10 Motoristas 

st.subheader(" Top 10 Motoristas por Score de Engajamento")

top10 = df.sort_values("score_engajamento", ascending=False).head(10)
top10 = top10.sort_values("driver_id", ascending=True)

st.dataframe(
    top10.style.applymap(lambda v: color_score(v, top10), subset=["score_engajamento"])
)


# Top 10 Motoristas Piores 

st.subheader(" Top 10 Motoristas Piores por Score de Engajamento")

piores10 = df.sort_values("score_engajamento", ascending=True).head(10)
piores10 = piores10.sort_values("driver_id", ascending=True)

st.dataframe(
    piores10.style.applymap(lambda v: color_score(v, piores10), subset=["score_engajamento"])
)


# Todos os motoristas 

st.subheader("Todos os Motoristas (Top 300 por Score)")

df_intervalo = df.sort_values("score_engajamento", ascending=False).head(300)
df_intervalo = df_intervalo.sort_values("driver_id", ascending=True)

st.dataframe(
    df_intervalo.style.applymap(lambda v: color_score(v, df_intervalo), subset=["score_engajamento"])
)
