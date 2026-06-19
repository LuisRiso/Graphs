def prim(matriz):
    vAtual = 0 #vertice inicial
    V = [i for i in range(len(matriz[0]))] #conjunto de vertices da matriz
    S = [vAtual] #conjunto de vertices jah selecionados pelo algoritmo
    N = [i for i in range(len(matriz[0]))] #conjunto de vertices não selecionados pelo algoritmo
    N.remove(vAtual)
    T = [] #conjunto de arestas que constituem a AGM
    peso = 0
    while len(T) < len(V) - 1:
        menorPeso = 99 #maiorPeso = -999 p/ arvore geradora maxima
        v = None
        u = None
        for i in S:
            for j in N:
                if matriz[i][j] > 0 and matriz[i][j] < menorPeso: #matriz[i][j] > maiorPeso p/ arvore gerado maxima
                    menorPeso = matriz[i][j]
                    v = i
                    u = j
        S.append(u)
        N.remove(u)
        T.append((v,u))
        peso = peso + menorPeso
    print(f'{T} {peso}')
                
prim([[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]])

