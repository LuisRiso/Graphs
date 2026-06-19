def kruskal(matriz):
    # Conjunto de vértices
    V = [i for i in range(len(matriz))]
    # 1) Montar lista de arestas H = (peso, v, u) em ordem crescente
    H = []
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):  # i+1 para não repetir (i,j) e (j,i)
            if matriz[i][j] > 0:             # se existe aresta
                H.append((matriz[i][j], i, j))
    H.sort()  # ordena por peso w_vu | reverse=True para arvore geradora maxima
    # 2) Estrutura Union-Find para detectar ciclos
    pai = [i for i in range(len(matriz))]
    rank = [0 for _ in range(len(matriz))]
    def find(v):
        # encontra representante do conjunto do vértice v
        if pai[v] != v:
            pai[v] = find(pai[v])  # compressão de caminho
        return pai[v]
    def union(a, b):
        # une os conjuntos de a e b, se forem diferentes
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False  # já estão no mesmo conjunto → criaria ciclo
        # união por rank
        if rank[ra] < rank[rb]:
            pai[ra] = rb
        elif rank[ra] > rank[rb]:
            pai[rb] = ra
        else:
            pai[rb] = ra
            rank[ra] += 1
        return True
    # 3) Kruskal em si
    T = []          # arestas da AGM
    pesoTotal = 0   # soma dos pesos
    i = 0
    while len(T) < len(V) - 1 and i < len(H):
        peso, v, u = H[i]
        i += 1
        # if T ∪ {v,u} != ciclo  → se union retorna True, não houve ciclo
        if union(v, u):
            T.append((v, u))
            pesoTotal += peso
            #print(f'Aresta adicionada: ({v}, {u}) com peso {peso}')
            #print(f'T = {T}')
            #print(f'pesoTotal = {pesoTotal}\n')
    print(f'{T} {pesoTotal}')
    return T, pesoTotal
