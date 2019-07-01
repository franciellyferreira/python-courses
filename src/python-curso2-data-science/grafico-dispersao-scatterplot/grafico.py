# -*- coding: utf-8 -*-

# Visualização de dados em Python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

titulo = "Scatterplot - Gráfico de Dispersão"
eixox  = "Eixo X"
eixoy  = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y)
plt.show()