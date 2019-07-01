# -*- coding: utf-8 -*-

"""
Escreva um programa que ordene uma lista numérica com três elementos. 
"""

elem1 = input("Informe o elemento 1: ")
elem2 = input("Informe o elemento 2: ")
elem3 = input("Informe o elemento 3: ")

lista = []
lista.append(int(elem1))
lista.append(int(elem2))
lista.append(int(elem3))

lista.sort()

print(lista)