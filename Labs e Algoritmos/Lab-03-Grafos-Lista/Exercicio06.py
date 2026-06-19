# Função: removeAresta(listaAdj, vi, vj)

# Descrição: Remove uma aresta no grafo considerando o par de vértices vi e vj.

# Entrada: lista de adjacências

# Saída: lista de adjacências com a aresta removida. (Obs. Considere a existência de grafos direcionados e não direcionados)

def removeArestaLista(listaAdj, vi, vj):

    controlador = '0'

    #Verifica se eh dirigido
    for vertice in listaAdj:
        for verticeAssociado in listaAdj[vertice]:
            if vertice not in listaAdj[verticeAssociado]:
                controlador = '1'
    
    if controlador == '0':
        listaAdj[vi].remove(vj)
        listaAdj[vj].remove(vi)

    else:
        listaAdj[vi].remove(vj)
    
    print(listaAdj)