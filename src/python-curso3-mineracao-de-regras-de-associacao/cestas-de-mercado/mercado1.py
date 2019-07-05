# -*- coding: utf-8 -*-
import pandas as pd

# Obtem dados do arquivo .csv
dados = pd.read_csv('mercado1.csv', header = None)

transacoes = []
for i in range(0,10):
    transacoes.append([str(dados.values[i, j]) for j in range(0,4)])

# Importa o algoritmo Apriori
from apyori import apriori
regras = apriori(transacoes, min_support = 0.3, min_confidence = 0.8, min_lift = 2, min_lenght = 2)

resultados  = list(regras)
resultados2 = [list(x) for x in resultados]

# Formata os dados para melhor exibicao
resultadoFormatado = []
for j in range(0,3):
    resultadoFormatado.append([list(x) for x in resultados2[j][2]])
print(resultadoFormatado)