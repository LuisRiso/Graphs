def dfs(residual, source, sink, visited, path):
    if source == sink:
        return True
    
    visited.add(source)
    
    for v in residual[source]:
        if residual[source][v] > 0 and v not in visited:
            path[v] = source
            if dfs(residual, v, sink, visited, path):
                return True
            
    return False


def ford_fulkerson(graph, source, sink):
    # Cria grafo residual
    residual = {u: {} for u in graph}
    for u in graph:
        for v in graph[u]:
            residual[u][v] = graph[u][v]
            if v not in residual:
                residual[v] = {}
            if u not in residual[v]:
                residual[v][u] = 0

    max_flow = 0

    while True:
        visited = set()
        path = {}
        
        found_path = dfs(residual, source, sink, visited, path)
        if not found_path:
            break

        # Calcula gargalo do caminho encontrado
        flow = float("inf")
        v = sink
        while v != source:
            u = path[v]
            flow = min(flow, residual[u][v])
            v = u

        # Atualiza residual
        v = sink
        while v != source:
            u = path[v]
            residual[u][v] -= flow
            residual[v][u] += flow
            v = u

        max_flow += flow

    return max_flow, residual

graph = {
    'A': {'B': 16, 'D': 13},
    'B': {'C': 12, 'D': 4},
    'C': {'D': 9, 'F': 20},
    'D': {'B': 10, 'E': 14},
    'E': {'C': 7, 'F': 4},
    'F': {}
}

max_flow, residual = ford_fulkerson(graph, 'A', 'F')

print("Fluxo máximo:", max_flow)
print("Residual final:")
for u in residual:
    print(u, residual[u])
