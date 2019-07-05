# -*- coding: utf-8 -*-
import pandas as pd

# Obtem dados do arquivo .csv
dados = pd.read_csv('mercado2.csv', header = None)

transacoes = []
for i in range(0,7501):
    transacoes.append([str(dados.values[i, j]) for j in range(0,20)])

# Importa o algoritmo Apriori
from apyori import apriori
regras = apriori(transacoes, min_support = 0.003, min_confidence = 0.2, min_lift = 3.0, min_lenght = 2)

resultados  = list(regras)
resultados2 = [list(x) for x in resultados]

# Formata os dados para melhor exibicao
resultadoFormatado = []
for j in range(0,5):
    resultadoFormatado.append([list(x) for x in resultados2[j][2]])
print(resultadoFormatado)