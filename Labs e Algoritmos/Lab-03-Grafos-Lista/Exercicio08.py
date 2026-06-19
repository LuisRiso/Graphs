# Função: verificaAdjacenciaLista(listaAdj, vi, vj)

# Descrição: Verifica se os vértices vi e vj são adjacentes

# Entrada: lista de adjacências

# Saída: True se vértices são adjacentes, False caso contrário (Boolean)

def verificaAdjacenciaLista(listaAdj, vi, vj):
    controlador = '0'

    #Verifica se eh dirigido
    for vertice in listaAdj:
        for verticeAssociado in listaAdj[vertice]:
            if vertice not in listaAdj[verticeAssociado]:
                controlador = '1'
    
    if controlador == '0':
        if vj in listaAdj[vi] and vi in listaAdj[vj]:
            print(True)
        else:
            print(False)
    
    else:
        if vj in listaAdj[vi] or vi in listaAdj[vj]:
            print(True)
        else:
            print(False)