# Função: Busca em Largura
# Descrição: Obtém a sequência dos vértices visitados conforme a Busca em Largura (Breadth First Search, BFS).
# Entrada: lista de adjacências (Dictionary)
# Saída: Lista de inteiros com a sequência dos vértices visitados (List [Integer])

# Por exemplo:

# Teste: BFS({0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}, 0)
# Input: {0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}, 0
# Resultado: [0, 1, 3, 4, 2, 5]

# listaAdjascencia eh um dicionario

def BFS(listaAdjascencia, verticeInicial):
    verticesAnalisados = [] #analisados
    filaDeControle = [] #visitados
    idsAnalisados = list(listaAdjascencia.keys()) #nao-visitados

    visitando = idsAnalisados.pop(verticeInicial)
    filaDeControle.append(visitando)

    while len(filaDeControle) != 0:
        
        for adjacente in listaAdjascencia[visitando]:
            if adjacente not in filaDeControle and adjacente not in verticesAnalisados:
                filaDeControle.append(adjacente)
                idsAnalisados.remove(adjacente)
        
        verticesAnalisados.append(visitando)
        filaDeControle.remove(visitando)


        if len(filaDeControle) != 0:
            visitando = filaDeControle[0]                
        
        if len(idsAnalisados) != 0 and len(filaDeControle) == 0:
            visitando = idsAnalisados[0]
            filaDeControle.append(visitando)
            idsAnalisados.remove(visitando)

        if len(idsAnalisados) == 0 and len(filaDeControle) == 0:
            break
    
    print(verticesAnalisados)

BFS({0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}, 0)