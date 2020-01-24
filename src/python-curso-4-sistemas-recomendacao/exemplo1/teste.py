from recomendacao import avaliacoes
from math import sqrt


# Testes de acesso aos dados de avaliação
print(avaliacoes['Ana']['Star Trek'])
print(avaliacoes['Marcos']['Star Trek'])
print(avaliacoes['Ana'])
print(avaliacoes['Leonardo'])


# Cálculo da distancia Euclidiana
distancia_ana_claudia = sqrt(pow(3 - 3, 2) + pow(3.5 - 4, 2))
print(distancia_ana_claudia)

distancia_ana_marcos = sqrt(pow(3 - 1.5, 2) + pow(3.5 - 5, 2))
print(distancia_ana_marcos)
