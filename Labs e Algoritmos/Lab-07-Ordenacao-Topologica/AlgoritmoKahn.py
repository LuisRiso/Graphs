def ordenacaoTopologicaKahn(listaAdj):
    # Calcula grau de entrada
    for v in listaAdj:
        for w in listaAdj[v]:
            indeg[w] += 1

    # 2) S = vértices com grau de entrada 0
    S = []
    for v in range(len(indeg)):
        if indeg[v] == 0:
            S.append(v)

    # 3) E = total de arestas (só conta as que existem como saídas nas chaves)
    E = 0
    for v in listaAdj:
        E += len(listaAdj[v])

    # 4) Loop principal
    L = []
    while len(S) != 0:
        # remove como fila simples
        v = S.pop(0)
        L.append(v)
        vizinhos = listaAdj[v]
        # print("vizinhos")
        # print(vizinhos)

        for w in vizinhos:
            print(f'w = {w}')
            E -= 1
            indeg[w] -= 1
            if indeg[w] == 0:
                S.append(w)

    # 5) Checagem de ciclo
    if E != 0:
        return None  # "NAO DAG"

    print(L)
    return



lista1 = {0: [1], 1: [], 2: [0], 3: [1, 2], 4: [1, 2]}
#lista2 = {0: [1, 3], 1: [2], 2: [], 3: [2], 4: [], 5: [6, 7], 6: [3, 7], 7: [], 8: [7]}
#lista3 = {0: [1, 3, 5], 1: [2], 2: [3, 4], 3: [], 4: [6], 5: [4, 6], 6: [7, 8], 7: [8], 8: [], 9: [6]}
#lista4 = {0:[1,2], 1:[3], 2:[3], 3:[]}
ordenacaoTopologicaKahn(lista1)
#ordenacaoTopologicaKahn(lista2)
#ordenacaoTopologicaKahn(lista3)
#ordenacaoTopologicaKahn(lista4)

