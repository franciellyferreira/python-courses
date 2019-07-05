# -*- coding: utf-8 -*-

# Crescimento da População Brasileira 1980-2016
# DataSus

import matplotlib.pyplot as plt

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

titulo = "Crescimento da População Brasileira 1980-2016"
eixox  = "Ano"
eixoy  = "População x 100.000.000"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x, y, color="#e4e4e4")
plt.plot(x, y, color="k", linestyle="--")
plt.show()