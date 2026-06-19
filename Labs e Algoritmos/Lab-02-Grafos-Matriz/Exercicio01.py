# Função: verificaAdjacencia(matriz, vi, vj)
# Descrição: Verifica se os vértices vi e vj são adjacentes
# Entrada: matriz de adjacências
# Saída: True se vértices são adjacentes, False caso contrário (Boolean)

import numpy as np

def verificaAdjacencia(matrizAdjacente, vi, vj):
    controle = False

    if matrizAdjacente[vi][vj] > 0:
        controle = True
    
    else:
        if matrizAdjacente[vj][vi] > 0:
            controle = True

    print(controle)
