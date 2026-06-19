# Função: Busca em Profundidade
# Descrição: Obtém a sequência dos vértices visitados conforme a Busca em Profundidade (Deep First Search, DFS).
# Entrada: lista de adjacências (Dictionary)
# Saída: Lista de inteiros com a sequência dos vértices visitados (List [Integer])
# Por exemplo:
# Teste: DFS({0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}, 0)
# Input: {0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}, 0
# Resultado: [0, 1, 2, 3, 4, 5]


def DFS(listaGrafo, verticeInicial):
    dfs = []
    idsVertices = list(listaGrafo.keys())
    deepFirstSearch(listaGrafo, verticeInicial, dfs, idsVertices)
    if idsVertices:
        for id in idsVertices:        
            deepFirstSearch(listaGrafo, id, dfs, idsVertices)
    print(dfs)

def deepFirstSearch(listaGrafo, visitando, dfs, idsVertices):
    dfs.append(visitando)
    idsVertices.remove(visitando)
    for adjacente in listaGrafo[visitando]:
        if adjacente not in dfs:
            deepFirstSearch(listaGrafo, adjacente, dfs, idsVertices)
    

lista1 = {0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}
lista2 = {0: [1, 2, 6], 1: [0, 3, 4], 2: [0, 6, 7], 3: [1, 4, 5], 4: [1, 3, 5], 5: [3, 4], 6: [0, 2, 7], 7: [2, 6]}
lista3 = {0: [1, 4, 7, 8], 1: [0, 2], 2: [1, 3, 4, 5], 3: [2, 5, 6], 4: [0, 2, 7, 9], 5: [2, 3, 6], 6: [3, 5], 7: [0, 4, 8, 9, 10], 8: [0, 7, 10], 9: [4, 7], 10: [7, 8]}
lista4 = {0: [2, 3], 1: [2, 3], 2: [0, 1, 3, 7], 3: [0, 1, 2, 5, 6], 4: [5, 6], 5: [3, 4, 6], 6: [3, 4, 5], 7: [2]}
lista5 = {0: [2, 4], 1: [2, 4], 2: [0, 1, 4], 3: [], 4: [0, 1, 2, 5, 6], 5: [4, 6], 6: [4, 5]}
lista6 = {0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]}

DFS(lista1, 0)
DFS(lista2, 0)
DFS(lista3, 0)
DFS(lista4, 0)
DFS(lista5, 0)
DFS(lista6, 3)