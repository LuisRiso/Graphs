import numpy as np
def bellman_ford(matrizAdj, v_i, v_f):
    matrizNP = np.array(matrizAdj)
    n = matrizNP.shape[0]
    # 1) Inicialização
    custo = []
    rota = []
    for _ in range(n):
        custo.append(9999)      # "infinito"
        rota.append(v_i)        # pai padrão
    custo[v_i] = 0
    rota[v_i] = None
    # 2) Relaxa todas as arestas |V|-1 vezes
    for k in range(n - 1):
        for v in range(n): #para cada aresta (v, u) em E
            for u in range(n):
                w_vu = matrizNP[v][u]
                # se existe aresta v -> u
                if w_vu != 0 and custo[v] != 9999:
                    if custo[u] > custo[v] + w_vu:
                        custo[u] = custo[v] + w_vu
                        rota[u] = v
    # 3) Verificação de ciclo negativo
    for v in range(n):
        for u in range(n):
            w_vu = matrizNP[v][u]
            if w_vu != 0 and custo[v] != 9999:
                if custo[u] > custo[v] + w_vu:
                    return False
    # 4) Reconstrução do caminho v_i -> v_f
    caminho = [v_f]
    anterior = rota[v_f]
    if custo[v_f] == 9999: #se custo[v_f] ficou infinito, não há caminho
        return None
    while anterior is not None:
        caminho.insert(0, anterior)
        anterior = rota[anterior]
    print(f'{caminho} {custo[v_f]}')
    return caminho, custo[v_f]

matriz = [
[0, 6, 0, 7, 0], 
[0, 0, 5, 8, -4], 
[0, -2, 0, 0, 0], 
[0, 0, -3, 0, 9], 
[2, 0, 7, 0, 0] 
]

bellman_ford(matriz, 0, 4)