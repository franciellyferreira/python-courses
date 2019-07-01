# -*- coding: utf-8 -*-

lista = [120, 6, 383, 19, 293, 90, 37, 2, 1, 9, 90]

# Ordena e não retorna
lista.sort()
print(lista)

# Ordena, não retorna e inverte
lista.sort(reverse=True)
print(lista)

# Inverte sem ordenar
lista.reverse()
print(lista)

# Ordena e retorna lista ordenada
lista_ordenada = sorted(lista)
print(lista_ordenada)

lista2 = ["bola","abacate","dinheiro"]

lista2.sort()
print(lista2)