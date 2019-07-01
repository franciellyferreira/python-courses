# -*- coding: utf-8 -*-

"""
Faça um programa que receba duas notas digitadas pelo usuário. 
Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.
"""

nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))

total = (nota1 + nota2) / 2

if total >= 6:
    print("Aprovado")

else:
    print("Reprovado")