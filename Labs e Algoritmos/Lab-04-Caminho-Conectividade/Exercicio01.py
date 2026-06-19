# Função: caminhoEuleriano(matriz)

# Descrição: Verifica se um grado possui um Caminho Euleriano.

# Entrada: matriz de adjacências (numpy nd.array)

# Saída: True se existe caminho Euleriano, False caso contrário.

# Teste: caminhoEuleriano([[0, 2, 2, 1], [2, 0, 0, 1], [2, 0, 0, 1], [1, 1, 1, 0]])

# Input: [[0, 2, 2, 1], [2, 0, 0, 1], [2, 0, 0, 1], [1, 1, 1, 0]]

# Resultado: Resultado

import numpy as np

def caminhoEuleriano(matrizRecebida):
    matrizRecebida = np.array(matrizRecebida)
    verticesGrafo = matrizRecebida.shape[0]
    TotalGrauVerticeImpar = 0
    i = 0

    while TotalGrauVerticeImpar <= 2 and i < verticesGrafo:
        grauVertice = 0
        for j in range(verticesGrafo):
            grauVertice += matrizRecebida[i][j]
    
        if grauVertice % 2 == 1:
            TotalGrauVerticeImpar += 1

        i += 1

        if grauVertice == 0:
            print("False")
            return
        
    if TotalGrauVerticeImpar == 1 or TotalGrauVerticeImpar > 2:
        print("False")
    
    else:
        print("True")

    

caminhoEuleriano([[0, 2, 2, 1], [2, 0, 0, 1], [2, 0, 0, 1], [1, 1, 1, 0]])

caminhoEuleriano([
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, 0]  
])

caminhoEuleriano([
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
])

caminhoEuleriano([
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0]
])


