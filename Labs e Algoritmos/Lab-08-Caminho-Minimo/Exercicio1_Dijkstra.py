import numpy as np
def dijkstra(matrizAdj, v_i, v_f):
    matrizNP = np.array(matrizAdj)
    custo = []
    rota = []
    for _ in range(matrizNP.shape[0]):
        custo.append(9999)
        rota.append(v_i)
    custo[v_i] = 0
    rota[v_i] = None
    vAbertos = [i for i in range(matrizNP.shape[0])]
    vFechados = []
    vAtual = v_i
    while vAbertos != []:
        vFechados.append(vAtual)
        vAbertos.remove(vAtual)
        vizinhos = [] #N do pseudocodigo
        for j in range(matrizNP.shape[0]):
            if matrizNP[vAtual][j] > 0:
                vizinhos.append(j)
        adjDisponiveis = set(vizinhos) - set(vFechados)
        for adj in adjDisponiveis:
            if matrizNP[vAtual][adj] > 0:
                if custo[vAtual] + matrizNP[vAtual][adj] < custo[adj]:
                    custo[adj] = custo[vAtual] + matrizNP[vAtual][adj]
                    rota[adj] = vAtual
        menor = 9999
        for i in vAbertos: 
            if custo[i] < menor:
                menor = custo[i]
                vAtual = i
    caminho = []
    caminho.append(v_f)
    anterior = rota[v_f]
    while anterior != None:
        caminho.insert(0, anterior)
        anterior = rota[anterior]
    print(f'{caminho} {custo[v_f]}')




#matriz1 = [[0, 10, 0, 5, 0], [0, 0, 1, 2, 0], [0, 0, 0, 0, 4], [0, 3, 9, 0, 2], [0, 0, 6, 0, 0]] 
#dijkstra(matriz1, 0, 2)


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

#dijkstra([[0, 3, 8, 4, -1, 10], [ 3, 0, -1, 6, -1, -1], [ 8, -1, 0, -1, 7, -1], [ 4,  6, -1, 0,  1,  3], [-1, -1,  7,  1, 0, 1], [10, -1, -1,  3,  1, 0]], 0, 5)
