import pandas as pd


# Carregar dados

df = pd.read_csv("data/drivers.csv")


# Score de engajamento

df["score_engajamento"] = (
    df["corridas_semana"] * 0.4 +
    df["horas_ativas"] * 0.3 +
    df["taxa_aceitacao"] * 100 * 0.2 -
    df["taxa_cancelamento"] * 100 * 0.1
)


# Classificação

def classificar(score):
    if score >= 65:
        return "Alto"
    elif score >= 35:
        return "Médio"
    else:
        return "Baixo"

df["nivel_engajamento"] = df["score_engajamento"].apply(classificar)


# Salvar CSV tratado

df.to_csv("outputs/drivers_com_engajamento.csv", index=False)

print("✅ drivers_com_engajamento.csv gerado com sucesso!")
