# Função: removeVertice(matriz, v)
# Descrição: Remove um dado vértice do grafo.
# Entrada: matriz de adjacências
# Saída: matriz de adjacências com o vértice removido.

import numpy as np

def removeVertice(matrizAdjacente, vi):
    quantidadeVertices = np.shape(matrizAdjacente)[0]

    for i in range(0, quantidadeVertices):
        matrizAdjacente[vi][i] = -1 #coluna
        matrizAdjacente[i][vi] = -1 #linha

    print(np.array(matrizAdjacente))