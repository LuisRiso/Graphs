def dfs(residual, u, t, visited, parent):
    visited[u] = True
    if u == t:
        return True
    n = len(residual)
    for v in range(n):
        if residual[u][v] > 0 and not visited[v]:
            parent[v] = u
            if dfs(residual, v, t, visited, parent):
                return True
    return False


def ford_fulkerson_matrix(graph, s, t):
    n = len(graph)

    # Copiando a matriz original para ser o residual
    residual = [row[:] for row in graph]

    max_flow = 0

    while True:
        visited = [False] * n
        parent = [-1] * n

        if not dfs(residual, s, t, visited, parent):
            break  # nenhum caminho aumentante

        # Calcula gargalo
        flow = float("inf")
        v = t
        while v != s:
            u = parent[v]
            flow = min(flow, residual[u][v])
            v = u

        # Atualiza residual
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= flow
            residual[v][u] += flow
            v = u

        max_flow += flow

    return max_flow, residual

graph_matrix = [
    [0, 16, 0, 13, 0, 0],   # A
    [0, 0, 12, 4, 0, 0],    # B
    [0, 0, 0, 9, 0, 20],    # C
    [0, 10, 0, 0, 14, 0],   # D
    [0, 0, 7, 0, 0, 4],     # E
    [0, 0, 0, 0, 0, 0]      # F
]

max_flow, residual = ford_fulkerson_matrix(graph_matrix, 0, 5)

print("Fluxo máximo =", max_flow)
print("Residual final:")
for row in residual:
    print(row)
