# Função: removeAresta(matriz, vi, vj)
# Descrição: Remove uma aresta no grafo considerando o par de vértices vi e vj.
# Entrada: matriz de adjacências
# Saída: matriz de adjacências com a aresta removida.

def removeAresta(matrizAdjacente, vi, vj):
    if matrizAdjacente[vi][vj] > 0:
        matrizAdjacente[vi][vj] -= 1

    if matrizAdjacente[vj][vi] > 0:
        matrizAdjacente[vj][vi] -= 1
    
    print(matrizAdjacente)