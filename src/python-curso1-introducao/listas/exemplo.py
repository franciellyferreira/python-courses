# -*- coding: utf-8 -*-

minha_lista_1 = ["abacaxi", "maca", "abacate"]
minha_lista_2 = [1, 2, 3, 4, 5]
minha_lista_3 = ["abacaxi", 2, 9.89, True]

print(minha_lista_1)
print(minha_lista_2)
print(minha_lista_3)

# Lista com índices
print(minha_lista_1[2])

# Lista com FOR
for item in minha_lista_1:
    print(item)

# Lista com WHILE e LEN
tamanho  = len(minha_lista_3)
contador = 1

while contador <= tamanho:
    print(contador)
    contador += 1

# Adiciona elemento na lista
minha_lista_1.append("banana")
print(minha_lista_1)

# Verifica se elemento se encontra na lista
if 5 in minha_lista_2:
    print("5 está na minha lista")

# Remover elementos da lista
del minha_lista_2[3:]
print(minha_lista_2)

# Apaga todos os elementos da lista
del minha_lista_2[:]
print(minha_lista_2)

# Lista em branco
minha_lista_4 = []
minha_lista_4.append(1)
print(minha_lista_4)