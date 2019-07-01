# -*- coding: utf-8 -*-

import aleatorio as a
import media     as m

lista = a.geraListaInteiro(4)
print("Minha lista:")
print(lista)

media = m.media(lista)
print("Média:")
print(media)

mediana = m.mediana(lista)
print("Mediana:")
print(mediana)

moda = m.moda(lista)
print("Moda:")
print(moda)