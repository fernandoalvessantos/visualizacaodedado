import matplotlib.pyplot as plt
from pathlib import Path

baseFolder = Path("/home/fernando.santos/desenvolvimento/pessoal/visualizacao-de-dados/base/")
saidaFolder = Path("/home/fernando.santos/desenvolvimento/pessoal/visualizacao-de-dados/saida/")
fileBacteria = baseFolder / "bacteria.fasta"
fileHumano = baseFolder / "human.fasta"
dados = open(fileHumano).read()
# fileout = saidaFolder / "bacteria.html"
fileout = saidaFolder / "humano.html"
saida = open(fileout, "w")

cont = {}

dados = dados.replace("\n", "")

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i + j] = 0

for k in range(len(dados) - 1):
    cont[dados[k] + dados[k + 1]] += 1

i = 1
for k in cont:
    transparencia = cont[k] / max(cont.values())
    saida.write("<div style='width:100px; border:1px solid #111; color: #FFFF; height: 100px;"
                "float:left; background-color:rgba(0,0,0," + str(transparencia) + "')>"+k+"</div>")
    if i % 4 == 0:
        saida.write("<div style='clear:both'></div>")

    i += 1

saida.close()
