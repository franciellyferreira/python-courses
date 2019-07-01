# -*- coding: utf-8 -*-

nome = "exemplo.txt"

# Modo leitura
modo = "r"

# Abre o arquivo
arquivo = open(nome, modo)

# Lê o arquivo
print(arquivo.read())

# Lê o arquivo e cria lista com cada linha do arquivo
print(arquivo.readlines())