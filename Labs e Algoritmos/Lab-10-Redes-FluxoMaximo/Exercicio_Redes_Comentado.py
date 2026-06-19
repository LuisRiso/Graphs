def dfs(residual, source, sink, visited, parent):
    """
    Executa DFS no grafo residual procurando um caminho aumentante.
    Retorna True se encontrou caminho até o sink.
    Preenche o dicionário 'parent' com o predecessor de cada nó.
    """
    visited.add(source)

    if source == sink:
        return True

    for v in residual[source]:
        if residual[source][v] > 0 and v not in visited:
            parent[v] = source
            if dfs(residual, v, sink, visited, parent):
                return True

    return False


def ford_fulkerson_verbose(graph, source, sink):
    """
    Implementa Ford–Fulkerson usando DFS e imprime, a cada iteração:
      - caminho aumentante
      - gargalo
      - atualizações no residual
      - grafo 'original' (somente arestas originais, com capacidades restantes)
      - grafo residual completo (incluindo arestas reversas)
    """

    # ====== CRIA GRAFO RESIDUAL ======
    residual = {u: {} for u in graph}
    original_edges = set()  # para sabermos quais arestas existiam no grafo original

    for u in graph:
        for v in graph[u]:
            residual[u][v] = graph[u][v]
            original_edges.add((u, v))
            if v not in residual:
                residual[v] = {}
            if u not in residual[v]:
                residual[v][u] = 0

    iteration = 1
    max_flow = 0

    print("\n==================== INICIANDO FORD–FULKERSON (DFS) ====================\n")

    while True:
        visited = set()
        parent = {}

        found = dfs(residual, source, sink, visited, parent)
        if not found:
            print("\n❌ Nenhum caminho aumentante encontrado. Fim do algoritmo.\n")
            break

        # ====== RECONSTRUIR CAMINHO ======
        path = []
        v = sink
        while v != source:
            path.append(v)
            v = parent[v]
        path.append(source)
        path = list(reversed(path))

        # ====== CALCULAR GARGALO ======
        flow = float("inf")
        for i in range(len(path) - 1):
            u = path[i]
            w = path[i+1]
            flow = min(flow, residual[u][w])

        print(f"\n-------------------- ITERAÇÃO {iteration} --------------------")
        print(f" Caminho encontrado: {' → '.join(path)}")
        print(f" Gargalo (flow): {flow}")
        print(f" Fluxo acumulado antes da iteração: {max_flow}")

        # ====== ATUALIZANDO RESIDUAL ======
        print("\n Atualizações no residual:")
        for i in range(len(path) - 1):
            u = path[i]
            w = path[i+1]

            print(f"  - {u} → {w}: {residual[u][w]} - {flow} = {residual[u][w] - flow}")
            print(f"  - {w} → {u}: {residual[w][u]} + {flow} = {residual[w][u] + flow}")

            residual[u][w] -= flow
            residual[w][u] += flow

        max_flow += flow

        # ====== GRAFO "ORIGINAL" ATUALIZADO (só arestas originais) ======
        print("\n Grafo original (capacidades restantes nas arestas originais):")
        for u in sorted(residual.keys()):
            linha = {}
            for v in sorted(residual[u].keys()):
                if (u, v) in original_edges and residual[u][v] > 0:
                    linha[v] = residual[u][v]
            print(f"  {u}: {linha}")

        # ====== GRAFO RESIDUAL COMPLETO ======
        print("\n Matriz residual após atualização (inclui arestas reversas):")
        for u in sorted(residual.keys()):
            print(f"  {u}: {residual[u]}")

        iteration += 1

    print("\n==================== RESULTADO FINAL ====================")
    print(f"Fluxo máximo: {max_flow}")

    print("\nMatriz residual final:")
    for u in sorted(residual.keys()):
        print(f"  {u}: {residual[u]}")

    return max_flow, residual


graph = {
    'A': {'B': 16, 'D': 13},
    'B': {'C': 12, 'D': 4},
    'C': {'D': 9, 'F': 20},
    'D': {'B': 10, 'E': 14},
    'E': {'C': 7, 'F': 4},
    'F': {}
}

ford_fulkerson_verbose(graph, 'A', 'F')