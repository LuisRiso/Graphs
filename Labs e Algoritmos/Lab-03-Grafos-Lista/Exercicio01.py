# Função: criaListaAdjacencias(matriz)

# Descrição: Cria uma lista de adjacências de um grafo representado por uma matriz de adjacências.

# Entrada: matriz de adjacências

# Saída: lista de adjacências (tipo Dictionary)

def criaListaAdjacencias(matrizAdjacencia):
    dicionarioMatriz = {}
    #enumerate = pares (indice, elemento)
    for i, linhaMatriz in enumerate(matrizAdjacencia):

        listaDicionario = []

        for j, pesoElemento in enumerate(linhaMatriz):
            if pesoElemento > 0:
                # [j]: lista unitaria, ou seja, lista com um unico elemento
                # pesoElemento: numero de vezes que o valor unitario sera inserido na lista
                # Cria uma lista temporária de tamanho pesoElemento → pico de memória O(v).
                listaDicionario.extend([j] * pesoElemento)

        dicionarioMatriz[i] = listaDicionario
    
    print(dicionarioMatriz)