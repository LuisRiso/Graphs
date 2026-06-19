def dijkstra(matriz, v_i, v_f):
    n = len(matriz)

    custo = [float('inf')] * n
    rota = [None] * n
    visitado = [False] * n
    custo[v_i] = 0

    while True:
        vAtual = None
        for v in range(n):
            if not visitado[v] and (vAtual is None or custo[v] < custo[vAtual]):
                vAtual = v
        if vAtual is None:
            break

        visitado[vAtual] = True

        for adj in range(n):
            peso = matriz[vAtual][adj]
            if peso > 0 and not visitado[adj] and custo[vAtual] + peso < custo[adj]:
                custo[adj] = custo[vAtual] + peso
                rota[adj] = vAtual

    caminho = []
    atual = v_f
    while atual is not None:
        caminho.insert(0, atual)
        atual = rota[atual]

    print(f'{caminho} {custo[v_f]}')


matriz2 = [[0, 60, 54, 42, 0, 0, 0, 0, 0, 0], 
[60, 0, 0, 71, 0, 29, 0, 0, 0, 0], 
[54, 0, 0, 56, 67, 0, 0, 0, 0, 0], 
[42, 71, 56, 0, 26, 52, 87, 0, 0, 0], 
[0, 0, 67, 26, 0, 0, 70, 0, 73, 0], 
[0, 29, 0, 52, 0, 0, 20, 25, 0, 0], 
[0, 0, 0, 87, 70, 20, 0, 36, 59, 32], 
[0, 0, 0, 0, 0, 25, 36, 0, 0, 25], 
[0, 0, 0, 0, 73, 0, 59, 0, 0, 26], 
[0, 0, 0, 0, 0, 0, 32, 25, 26, 0]]
dijkstra(matriz2, 0, 9)