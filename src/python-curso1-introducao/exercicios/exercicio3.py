# -*- coding: utf-8 -*-

"""
Escreva um programa que resolva uma equação de segundo grau
"""

a = int(input("Informe o coeficiente a: "))
b = int(input("Informe o coeficiente b: "))
c = int(input("Informe o coeficiente c: "))

equacao = str(a) + "x² " + str(b) + "x " + str(c)
print("Equação:")
print(equacao)

# 1) Calcular o valor de Delta
delta = (b ** 2) + (-(4) * a * c)
print("Delta:")
print(delta)

# 2) Calcular os valores de X
x_positivo = (-b + (delta ** (1/2))) / (2 * a)
print("O valor de X positivo")
print(x_positivo)
x_negativo = (-b - (delta ** (1/2))) / (2 * a)
print("O valor de X negativo")
print(x_negativo)