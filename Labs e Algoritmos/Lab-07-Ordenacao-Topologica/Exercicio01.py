# Nome da Função: temposVertices(listaAdj, v)
# Descrição: Obtém o tempo de descoberta (TD) e o tempo de término (TT) de cada vértice de um grafo, a partir da análise dos adjacentes de um dado vértice inicial v considerando a Busca em Profundidade (Deep First Search, DFS).
# Entrada: lista de adjacências (Dictionary) e identificador (id) do vértice inicial v (Integer).
# Saída: Estrutura {chave : valor} (Dictionary), com a chave correspondendo ao id do vértice e o valor os tempos de descoberta (TD) e de término (TT) de cada vértice no formato {0: TD / TT, 1:TD/TT ..., n: TD/TT}. 
# Por exemplo:
# Teste: temposVertices({0: [1, 4], 1: [2, 4], 2: [5], 3: [0, 4], 4: [5], 5: [1]}, 0)
# Input: {0: [1, 4], 1: [2, 4], 2: [5], 3: [0, 4], 4: [5], 5: [1]}, 0
# Resultado: {0: '1/10', 1: '2/9', 2: '3/6', 3: '11/12', 4: '7/8', 5: '4/5'}

import numpy as np

def temposVertices(listaAdj, verticeInicial):
    #tamLista = len(listaAdj)
    cor = [0 for _ in range(len(listaAdj))]  # 0 = BRANCO
    tipoArest = [[0 for _ in range(len(listaAdj))] for _ in range(len(listaAdj))]
    tempoD = [0 for _ in range(len(listaAdj))]
    tempoT = [0 for _ in range(len(listaAdj))]
    tempo = [0]
    listaResultante = {}

    visitaDFS(listaAdj, verticeInicial, cor, tipoArest, tempoD, tempoT, tempo)
    for vertice in listaAdj:
        if cor[vertice] == 0:
            visitaDFS(listaAdj, vertice, cor, tipoArest, tempoD, tempoT, tempo)

    for vert in listaAdj:
        listaResultante[vert] = f'{tempoD[vert]}/{tempoT[vert]}'

    print(listaResultante)
    return

def visitaDFS(listaAdj, vertice, cor, tipoArest, tempoD, tempoT, tempo):
    tempo[0] = tempo[0] + 1
    cor[vertice] = 1  # cinza
    tempoD[vertice] = tempo[0]

    for adjacente in listaAdj[vertice]:
        if cor[adjacente] == 0:
            tipoArest[vertice][adjacente] = 0  # árvore
            visitaDFS(listaAdj, adjacente, cor, tipoArest, tempoD, tempoT, tempo)
        elif cor[vertice] == 1:
            tipoArest[vertice][adjacente] = 1  # back
        else:
            if tempoD[vertice] < tempoD[adjacente]:
                tipoArest[vertice][adjacente] = 2  # avanço
            else:
                tipoArest[vertice][adjacente] = 3  # cruzamento

    cor[vertice] = 2  # preto
    tempo[0] = tempo[0] + 1
    tempoT[vertice] = tempo[0]

lista1 = {0: [1, 4], 1: [2, 4], 2: [5], 3: [0, 4], 4: [5], 5: [1]}
lista2 = {0: [1, 4], 1: [2, 4], 2: [3], 3: [1], 4: [3], 5: [0, 4]}
lista3 = {0: [1], 1: [], 2: [0], 3: [1, 2], 4: [1, 2]}
lista4 = {0: [1, 5], 1: [0, 4], 2: [3, 5, 7], 3: [2, 6, 7], 4: [1], 5: [0, 2, 7], 6: [3, 7], 7: [2, 3, 5, 6]}
lista5 = {0: [1, 4], 1: [2, 4], 2: [3], 3: [1], 4: [3], 5: [0, 4]}
lista6 = {0: [1, 5], 1: [0, 4], 2: [3, 5, 7], 3: [2, 6, 7], 4: [1], 5: [0, 2, 7], 6: [3, 7], 7: [2, 3, 5, 6]}
temposVertices(lista1, 0)
temposVertices(lista2, 0)
temposVertices(lista3, 0)
temposVertices(lista4, 0)
temposVertices(lista5, 3)
temposVertices(lista6, 4)