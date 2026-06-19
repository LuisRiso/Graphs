# Função: calcDensidade((listaAdj)
# 
# Descrição: Retorna o valor da densidade do grafo.
# 
# Entrada: lista de adjacências
# 
# Saída: Densidade com precisão de três casas decimais (float).

def calcDensidadeLista(listaAdj):
    controlador = '0'
    arestas = 0
    vertices = len(listaAdj)
    densidade = 0.0

    #Verifica se eh digrafo
    #Mantem controle = '0' se for simples
    for vertice in listaAdj:
        for verticeAssociado in listaAdj[vertice]:
            if vertice not in listaAdj[verticeAssociado]:
                controlador = '1'

    if controlador == '0':
        for vi in listaAdj:
            arestas += len(listaAdj[vi])
        densidade = arestas/(vertices*(vertices-1))
        print(f'{densidade:.3f}')

    else:
        for vi in listaAdj:
            arestas += len(listaAdj[vi])
        densidade = arestas/(vertices*(vertices-1))
        print(f'{densidade:.3f}')