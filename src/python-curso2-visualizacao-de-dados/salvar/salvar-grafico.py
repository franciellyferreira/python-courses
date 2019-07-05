# -*- coding: utf-8 -*-

# Visualização de dados em Python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 3000, 100]

titulo = "Scatterplot - Gráfico de Dispersão"
eixox  = "Eixo X"
eixoy  = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y, label="Minhas Linhas", color="k", linestyle="--")
plt.scatter(x, y, label="Meus Pontos", color="k", marker=".", s=z)
plt.legend()
# plt.show()
# plt.savefig("figura1.pdf")
plt.savefig("figura1.png", dpi=300)