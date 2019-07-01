# -*- coding: utf-8 -*-

""" 
Faça um programa que receba a idade do usuário 
e diga se ele é maior ou menor de idade.
"""

idade = input("Qual sua idade: ")

if int(idade) >= 18:
    print("Usuário é maior de idade.")
    
elif int(idade) > 0 and int(idade) < 18:
    print("Usuário é menor de idade") 

else:
    print("Usuário digitou idade inválida.")