# Função: insereAresta(listaAdj)

# Descrição: Insere uma aresta no grafo considerando o par de vértices vi e vj.

# Entrada: lista de adjacências

# Saída: lista de adjacências.

def insereArestaLista(listaAdj, i, j):
    controlador = '0'

    #Verifica se eh dirigido
    for vertice in listaAdj:
        for verticeAssociado in listaAdj[vertice]:
            if vertice not in listaAdj[verticeAssociado]:
                controlador = '1'
    
    #Insercao aresta se for simples
    if controlador == '0':
        listaAdj[i].append(j)
        listaAdj[j].append(i)
        listaAdj[i].sort()
        listaAdj[j].sort()
    
    #Insercao aresta se for dirigido
    else:
        listaAdj[i].append(j)
        listaAdj[i].sort()

    print(listaAdj)