# Função: tipoGrafo(listaAdj)

# Descrição: Retorna o tipo do grafo representado por uma dada lista de adjacências.

# Entrada: lista de adjacências

# Saída: Tipo do grafo (Integer) sendo: 0 - grafo simples; 1 - digrafo; 20 - multigrafo; 21 - multigrafo dirigido; 30 - pseudografo; 31 - pseudografo dirigido.

def tipoGrafoLista(listaAdj):

    controlador = '0'

    #Verifica se eh digrafo
    #Mantem controle = '0' se for simples
    for vertice in listaAdj:
        for verticeAssociado in listaAdj[vertice]:
            if vertice not in listaAdj[verticeAssociado]:
                controlador = '1'

    #Verifica multigrafo
    for vertices in listaAdj.values():
        # for verticeAssociado in listaAdj[vertice]:
        if len(vertices) != len(set(vertices)):
            controlador = '2' + controlador
            break
        # if controlador[0] == '2':
        #     break

        #Verifica pseudografo
    for vertice in listaAdj:
        if vertice in listaAdj[vertice]:
            controlador = '3' + controlador
            break
        if controlador[0] == '3':
            break

    print(controlador)

             
