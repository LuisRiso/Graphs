# Nome da Função: OrdenacaoTopologica(listaAdj)
# Descrição: Obtém a ordenação topológica de um grafo acíclico direcionado (DAG), com início em um dado vértice v.
# Entrada: lista de adjacências (Dictionary)
# Saída: Lista com os índices dos vértices conforme ordem topológica (List), ex. [5, 1, 2 ...].
# Por exemplo:
# Teste: ordenacaoTopologica({0: [1], 1: [], 2: [0], 3: [1, 2], 4: [1, 2]})
# Input: {0: [1], 1: [], 2: [0], 3: [1, 2], 4: [1, 2]}
# Resultado: [4, 3, 2, 0, 1]

def ordenacaoTopologica(listaAdj):
    v = 0
    sequencia = []
    tempo = [0]
    tempoE = [0 for _ in range(len(listaAdj))]
    tempoS = [0 for _ in range(len(listaAdj))]
    tipoAresta = [[0 for _ in range(len(listaAdj))] for _ in range(len(listaAdj))]
    cor = [0 for _ in range(len(listaAdj))]

    for v in listaAdj:
        if cor[v] == 0:
            dfsRecursiva(sequencia, tempo, v, tempoE, tempoS, tipoAresta, cor, listaAdj)

    print(sequencia)


def dfsRecursiva(sequencia, tempo, v, tempoE, tempoS, tipoAresta, cor, listaAdj):
    tempo[0] = tempo[0] + 1
    tempoE[v] = tempo[0]
    cor[v] = 1

    for adj in listaAdj[v]:
        if cor[adj] == 0:
            tipoAresta[v][adj] = 0
            dfsRecursiva(sequencia, tempo, adj, tempoE, tempoS, tipoAresta, cor, listaAdj)
        elif cor[adj] == 1:
            tipoAresta[v][adj] = 1
        else:
            if tempoE[v] < tempoE[adj]:
                tipoAresta[v][adj] = 2
            else:
                tipoAresta[v][adj] = 3

    tempo[0] = tempo[0] + 1
    cor[v] = 2
    tempoS[v] = tempo[0]
    sequencia.insert(0, v)

lista1 = {0: [1], 1: [], 2: [0], 3: [1, 2], 4: [1, 2]}
lista2 = {0: [1, 3], 1: [2], 2: [], 3: [2], 4: [], 5: [6, 7], 6: [3, 7], 7: [], 8: [7]}
lista3 = {0: [1, 3, 5], 1: [2], 2: [3, 4], 3: [], 4: [6], 5: [4, 6], 6: [7, 8], 7: [8], 8: [], 9: [6]}
ordenacaoTopologica(lista1)
ordenacaoTopologica(lista2)
ordenacaoTopologica(lista3)