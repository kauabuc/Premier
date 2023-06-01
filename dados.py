import pandas as pd

dados = pd.read_csv("projetos/PremierL/epl_results_2022-23.csv")


def formatar(valor):
    return "{:.2f}".format(valor)

# print(dados)
# print(dados.columns)

# print(dados.describe())
# print(dados.isnull().sum())


golsH = dados.groupby("HomeTeam")["FTHG"].sum()
golsA = dados.groupby("AwayTeam")["FTAG"].sum()
golsM = golsA + golsH

golsCH = dados.groupby("HomeTeam")["FTAG"].sum()
golsCA = dados.groupby("AwayTeam")["FTHG"].sum()
golsC = golsCA + golsCH

shotsMH = dados.groupby("HomeTeam")["HST"].sum()
shotsMA = dados.groupby("AwayTeam")["AST"].sum()
shotsM = (shotsMA + shotsMH) / 38

shotsCH = dados.groupby("HomeTeam")["AST"].sum()
shotsCA = dados.groupby("AwayTeam")["HST"].sum()
shotsC = (shotsCA + shotsCH) / 38

yellowH = dados.groupby("HomeTeam")["HY"].sum()
yellowA = dados.groupby("AwayTeam")["AY"].sum()
yellow = yellowH + yellowA


dadosnovos = pd.DataFrame()

dadosnovos["Teams"] = golsH.index
dadosnovos["GoalsM"] = golsM.values
dadosnovos["GoalsC"] = golsC.values
dadosnovos["Shots Per Game"] = shotsM.values
dadosnovos["ShotsC Per Game"] = shotsC.values
dadosnovos["Yellows"] = yellow.values

dadosnovos["Shots Per Game"] = dadosnovos["Shots Per Game"].apply(formatar)
dadosnovos["ShotsC Per Game"] = dadosnovos["ShotsC Per Game"].apply(formatar)

print(dadosnovos)
dadosnovos.to_csv("projetos/PremierL/novos_dados.csv",
                  encoding="utf-8")
