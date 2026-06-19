# Função: tipoGrafo(matriz)
# Descrição: Retorna o tipo do grafo representado por uma dada matriz de adjacências.
# Entrada: matriz de adjacências
# Saída: Tipo do grafo (Integer) sendo: 
# 0 - grafo simples; 
# 1 - digrafo; 
# 20 - multigrafo; 
# 21 - multigrafo dirigido; 
# 30 - pseudografo; 
# 31 - pseudografo dirigido.

import numpy as np

def tipoGrafo(matrizAdjacente):
    quantidadeVertices = np.shape(matrizAdjacente)[0] #vai entregar uma tupla com linha e coluna = neste caso sera [linha][0]
    controlador = '0'

    # diagonalPrincipal = np.diag(matrizAdjacente)
    # matrizSuperior = np.triu(matrizAdjacente, k=1) "k=1 inclusao diagonal"
    # matrizInferior = np.tril(matrizAdjacente, k=-1)
    
    #Teste para verificacao pseudografo
    for vertice_i in range(0, quantidadeVertices):
        for vertice_j in range(vertice_i + 1, quantidadeVertices):
            if matrizAdjacente[vertice_i][vertice_j] != matrizAdjacente[vertice_j][vertice_i]:
                controlador = '1'

    #Teste para verificacao pseudografo
    if np.sum(np.diagonal(matrizAdjacente)) > 0:
        controlador = '3' + controlador

    for vertice_i in range(0, quantidadeVertices):
        for vertice_j in range(0, quantidadeVertices):
            if matrizAdjacente[vertice_i][vertice_j] > 1:
                controlador = '2' + controlador
                break
        if controlador[0] == '2':
            break
    
    print(controlador)


