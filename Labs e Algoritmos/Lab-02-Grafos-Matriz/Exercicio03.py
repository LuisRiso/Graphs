# Função: calcDensidade(matriz)
# Descrição: Retorna o valor da densidade do grafo simples.
# Entrada: matriz de adjacências
# Saída: Valor da densidade com precisão de três casas decimais (Float)

import numpy as np

def calcDensidade(matrizAdjacente):

    quantidadeVertices = np.shape(matrizAdjacente)[0]

    matrizSuperior = np.triu(matrizAdjacente, k=1) 
    matrizInferior = np.tril(matrizAdjacente, k=-1)

    numeroArestas = 0
    controlador = '0'
    densidadeMatriz = 0.0

    if np.array_equal(matrizSuperior,matrizInferior.T) == False:
        controlador = '1'
    
    if controlador == '0':
        numeroArestas = np.sum(matrizSuperior)
        densidadeMatriz = (2*numeroArestas)/(quantidadeVertices*(quantidadeVertices-1))
        densidadeMatriz = round(densidadeMatriz,3)
    
    else:
        numeroArestas = np.sum(matrizAdjacente)
        densidadeMatriz = (numeroArestas)/(quantidadeVertices*(quantidadeVertices-1))
        densidadeMatriz = round(densidadeMatriz,3)
    
    print(densidadeMatriz)


