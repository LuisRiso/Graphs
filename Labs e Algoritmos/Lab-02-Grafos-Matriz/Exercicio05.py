# Função: insereVertice(matriz)
# Descrição: Insere um vertice no grafo.
# Entrada: matriz de adjacências
# Saída: matriz de adjacências com o vértice inserido.

# Usando Numpy

import numpy as np

def insereVertice(matrizAdjacente):
    matrizAdjacente = np.array(matrizAdjacente)  # garante que é array NumPy
    quantidadeVertices = matrizAdjacente.shape[0]
    
    # Cria uma nova matriz com uma linha e uma coluna a mais, preenchida com zeros
    novaMatriz = np.zeros((quantidadeVertices + 1, quantidadeVertices + 1), dtype=int)
    
    # Copia a matriz antiga para a nova
    novaMatriz[:quantidadeVertices, :quantidadeVertices] = matrizAdjacente
    
    print(novaMatriz)
    return novaMatriz


# Usando python puro

# import numpy as np

# def insereVertice(matrizAdjacente):
#     quantidadeVertices = np.shape(matrizAdjacente)[0]

#     for i in range(0, quantidadeVertices):
#         matrizAdjacente[i].append(0)
        
#     lista = [0] * (quantidadeVertices + 1)
#     matrizAdjacente.append(lista)

#     print(np.array(matrizAdjacente))

