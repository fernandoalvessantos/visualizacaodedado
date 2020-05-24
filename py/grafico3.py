import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 7, 1, 0]
z = [20, 30, 40, 600, 40]

titulo = "Scatterplot grafico de dispersao"
eixox = "Eixo X"
eixoy = "Eixo Y"
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
# plt.scatter(x1, y1, label = "Pontos", color = "r")
# outros marcadores
plt.scatter(x1, y1, label="Pontos", color="red", marker="h", s=z)
plt.plot(x1, y1, color="k", linestyle="--")
plt.legend()
# plt.show()
# SALVANDO FIGURA
plt.savefig("saida/figura1.png", dpi=300)
plt.savefig("saida/figura1.pdf") #PDF formato vetorial
