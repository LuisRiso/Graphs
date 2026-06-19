# Função: criaDicionario(matriz)
# Descrição: 
# A partir da matriz, implemente uma função que constrói um dicionário. 
# Cada chave do dicionário corresponde ao índice da linha da matriz. 
# O valor de cada chave corresponde a uma lista com os índices das colunas associadas à linha em questão, que possuam valor maior que 0. 
# Caso o valor da coluna seja maior que 1 deve-se repetir o índice da coluna conforme o valor 
# (ex. a célula dada pela linha 1 e coluna 2 tem valor 4, logo, o valor 2 na lista da linha 1 precisará ser repetido 4 vezes).
# Entrada: matriz de adjacências
# Saída: representação da matriz como Dictionary.
# Por exemplo:
# Teste: criaDicionario([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])
# Input: [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
# Resultado: {0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}


def criaDicionario(matriz):
    dicionarioMatriz = {}
    #enumerate = pares (indice, elemento)
    for i, linhaMatriz in enumerate(matriz):

        listaDicionario = []

        for j, pesoElemento in enumerate(linhaMatriz):
            if pesoElemento > 0:
                # [j]: lista unitaria, ou seja, lista com um unico elemento
                # pesoElemento: numero de vezes que o valor unitario sera inserido na lista
                # Cria uma lista temporária de tamanho pesoElemento → pico de memória O(v).
                listaDicionario.extend([j] * pesoElemento)

        dicionarioMatriz[i] = listaDicionario
    
    print(dicionarioMatriz)


# Outros jeitos de fazer pelo GPT

#Jeito 01 [Ideal]:
#Controi de uma vez o list comprehension sem usar memoria adicional e temporaria
#Costuma ser o mais rápido e simples
def construir_dic(matriz):
    dicionarioMatriz = {}
    for i, linhaMatriz in enumerate(matriz):
        # sintaxe de list comprehension
        # [EXPRESSÃO for VARS in ITERÁVEL if CONDIÇÃO  ... ]
        # j (à esquerda) é a EXPRESSÃO: é o valor que será colocado na lista resultante
        # j após o for é a variável de loop que você está desempacotando de enumerate(linhaMatriz)
        listaDicionario = [j for j, pesoElemento in enumerate(linhaMatriz) if pesoElemento > 0 for _ in range(pesoElemento)]
        dicionarioMatriz[i] = listaDicionario
    print(dicionarioMatriz)

#codigo expandido de
# [j for j, peso in enumerate(linhaMatriz) if peso > 0 for _ in range(peso)]
# resultado = []
# for j, pesoElemento in enumerate(linhaMatriz):
#     if pesoElemento > 0:
#         for _ in range(pesoElemento):
#             resultado.append(j)



#Jeito 02:
#Maneira sem usar lista temporaria e evita o loop Python
from itertools import repeat

def construir_dic(matriz):
    dicionarioMatriz = {}
    for i, linhaMatriz in enumerate(matriz):
        listaDicionario = []
        for j, pesoElemento in enumerate(linhaMatriz):
            if pesoElemento > 0:
                listaDicionario.extend(repeat(j, pesoElemento))
        dicionarioMatriz[i] = listaDicionario
    return dicionarioMatriz