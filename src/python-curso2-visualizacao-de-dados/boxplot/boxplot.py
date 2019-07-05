# -*- coding: utf-8 -*-

# Boxplot - Diagrama de Caixa

import matplotlib.pyplot as plt
import random

valores = []

for i in range(10):
    numero = random.randint(0,5)
    valores.append(numero)

plt.boxplot(valores)
plt.title('Meu Boxplot')
plt.show()