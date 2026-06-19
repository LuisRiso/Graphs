def dfs(residual, v, t, visitado, vizinho):
    visitado[v] = True
    if v == t:
        return True
    n = len(residual)
    #print(residual)
    for u in range(n):
        if residual[v][u] > 0 and not visitado[u]:
            vizinho[u] = v
            if dfs(residual, u, t, visitado, vizinho):
                return True
    return False


def ford_fulkerson_matrix(graph, s, t):
    n = len(graph)

    # Copiando a matriz original para ser o residual
    residual = [row[:] for row in graph]

    fluxoMax = 0

    while True:
        visitado = [False] * n
        vizinho = [-1] * n

        if not dfs(residual, s, t, visitado, vizinho):
            break  # nenhum caminho aumentante

        # Calcula gargalo
        fluxo = float("inf")
        v = t
        while v != s:
            u = vizinho[v]
            fluxo = min(fluxo, residual[u][v])
            v = u

        # Atualiza residual
        v = t
        while v != s:
            u = vizinho[v]
            residual[u][v] -= fluxo
            residual[v][u] += fluxo
            v = u

        fluxoMax += fluxo
    print("Fluxo máximo =", fluxoMax)
    return 

graph_matrix = [
    [0, 16, 0, 13, 0, 0],   # A
    [0, 0, 12, 4, 0, 0],    # B
    [0, 0, 0, 9, 0, 20],    # C
    [0, 10, 0, 0, 14, 0],   # D
    [0, 0, 7, 0, 0, 4],     # E
    [0, 0, 0, 0, 0, 0]      # F
]

ford_fulkerson_matrix(graph_matrix, 0, 5)
