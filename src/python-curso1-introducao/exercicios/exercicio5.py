# -*- coding: utf-8 -*-

"""
Escreva um programa que receba dois números e um sinal, 
e faça a operação matemática definida pelo sinal.  
"""

numeroA   = input("Digite um número: ")
numeroB   = input("Digite um número: ")
operacao  = input("Digite uma operação: ")

if operacao == "+":
    resultado = int(numeroA) + int(numeroB)
elif operacao == "-":
    resultado = int(numeroA) - int(numeroB)
elif operacao == "/":
    resultado = int(numeroA) / int(numeroB)
elif operacao == "*":
    resultado = int(numeroA) * int(numeroB)
elif operacao == "**":
    resultado = int(numeroA) ** int(numeroB)
elif operacao == "//":
    resultado = int(numeroA) // int(numeroB)
elif operacao == "%":
    resultado = int(numeroA) % int(numeroB)

print(resultado)