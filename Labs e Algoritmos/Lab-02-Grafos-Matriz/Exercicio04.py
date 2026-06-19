# Função: insereAresta(matriz)
# Descrição: Insere uma aresta no grafo considerando o par de vértices vi e vj.
# Entrada: matriz de adjacências
# Saída: matriz de adjacências.

def insereAresta(matrizAdjacente, vi, vj):
    matrizAdjacente[vi][vj] += 1
    matrizAdjacente[vj][vi] += 1
    print(matrizAdjacente)