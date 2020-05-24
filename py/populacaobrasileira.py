import matplotlib.pyplot as plt
from pathlib import Path

baseFolder= Path("/home/fernando.santos/desenvolvimento/pessoal/visualizacao-de-dados/base/")
saidaFolder= Path("/home/fernando.santos/desenvolvimento/pessoal/visualizacao-de-dados/saida/")
file = baseFolder / "pop_br_1980_2016.csv"
dados = open(file).readlines()

x=[]
y=[]
for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.plot(x,y)
plt.bar(x,y)

plt.title("Crescimento da População BR 1980 - 2016")
plt.xlabel("Ano")
plt.ylabel("População x 100 milhões")
plt.show()