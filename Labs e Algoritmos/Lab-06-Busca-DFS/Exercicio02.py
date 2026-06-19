# Função: Busca em Profundidade
# Descrição: Obtém a sequência dos vértices visitados conforme a Busca em Profundidade (Deep First Search, DFS) considerando uma implementação iterativa.
# Entrada: lista de adjacências (Dictionary)
# Saída: Lista de inteiros com a sequência dos vértices visitados (List [Integer])
# Por exemplo:
# Teste: DFS({0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}, 0)
# Input: {0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}, 0
# Resultado: [0, 1, 2, 3, 4, 5]

def DFS(listaGrafo, verticeInicial):

    idsVertices = list(listaGrafo.keys())
    dfs = []
    pilha = [verticeInicial]

    while len(idsVertices) != 0:
        print("teste 1: dfs dentro da lista")
        print(dfs)
        
        while len(pilha) != 0:
            #print("teste 2: dfs dentro da lista")
            #print(dfs)
            visitando = pilha[0]
            #print(visitando)

            if visitando not in dfs:
                dfs.append(visitando)
                #print("teste 3: dfs dentro da lista")
                #print(dfs)
            
            for adjacenteViavel in listaGrafo[visitando]:
                
                if adjacenteViavel not in dfs:
                    pilha.insert(0, adjacenteViavel)
                    #print("teste 4: dfs dentro da lista")
                    #print(dfs)
                
                else:
                    if len(pilha) != 0:
                        pilha.pop(0)
                    #print("teste 5: dfs dentro da lista")
                    #print(dfs)
        
        idsVertices = []
        for ids in listaGrafo.keys():
            if ids not in dfs:
                idsVertices.append(ids)
                #print("teste 6: dfs dentro da lista")
                #print(dfs)
        
        if len(idsVertices) != 0:
            pilha.inset(0, idsVertices[0])
        #print("dfs dentro da lista")
        #print(dfs)
    
    print(dfs)


lista1 = {0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}
DFS(lista1, 0)

