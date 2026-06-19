# Função: dimensaoMatriz
# Descrição: Retorna a dimensão da matriz no formato (linhas, colunas) e a lista com os valores da sua diagonal.
# Entrada: matriz de adjacências
# Saída: Dimensão da matriz (linhas, coluna), lista com valores da diagonal.
# Por exemplo:
# Teste: dimensaoMatriz([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]])
# Input: [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]]
# Resultado: (4, 4) [0 0 0 0]

def dimensaoMatriz(matriz):
    linhasMatriz = len(matriz)
    colunasMatriz = len(matriz[0])
    
    diagonalMatriz = []
    for i in range(min(linhasMatriz,colunasMatriz)):
        diagonalMatriz[i] = matriz[i][i]
    
    print(f"({linhasMatriz},{colunasMatriz}) {diagonalMatriz}")

#Jeito mais eficiente
def dimensaoMatriz(matriz):
    linhasMatriz = len(matriz)
    colunasMatriz = len(matriz[0])
    
    diagonalMatriz = [matriz[i][i] for i in range(min(linhasMatriz, colunasMatriz))]
    # for i in range(min(linhasMatriz,colunasMatriz)):
    #     diagonalMatriz[i] = matriz[i][i]
    
    print(f"({linhasMatriz}, {colunasMatriz})" + " " + "[" + " ".join(map(str, diagonalMatriz)) + "]") 

#Jeito que acabei pensando 
def dimensaoMatriz(matriz):
    linhasMatriz = len(matriz)
    colunasMatriz = len(matriz[0])
    
    diagonalMatriz = [0] * min(linhasMatriz, colunasMatriz)
    for i in range(min(linhasMatriz,colunasMatriz)):
        diagonalMatriz[i] = matriz[i][i]
    
    print(f"({linhasMatriz}, {colunasMatriz})" + " " + "[" + " ".join(map(str, diagonalMatriz)) + "]") 

# Jeito sugerido pelo GPT:
def dimensaoMatriz(matriz):
    #Trata matriz vazia
    if not matriz:
        print("(0, 0) []")
        return

    linhasMatriz = len(matriz)
    colunasMatriz = len(matriz[0])

    #Garantir que é retangular (opcional)
    if any(len(l) != colunasMatriz for l in matriz):
        raise ValueError("Matriz irregular (linhas de tamanhos diferentes).")

    #Constrói a diagonal corretamente
    diagonalMatriz = [matriz[i][i] for i in range(min(linhasMatriz, colunasMatriz))]

    #Formata igual ao exemplo: [0 0 0 0]
    diag_str = "[" + " ".join(map(str, diagonalMatriz)) + "]"
    print(f"({linhasMatriz}, {colunasMatriz}) {diag_str}")


#Implementação “estrita” (boa para matriz de adjacência)
#Valida que é retangular; opcionalmente valida que é quadrada.
def dimensaoMatriz(matriz):
    if not matriz:
        return (0, 0), []

    linhas = len(matriz)
    colunas = len(matriz[0])

    # Verifica retangularidade
    if any(len(l) != colunas for l in matriz):
        raise ValueError("Matriz irregular (linhas com comprimentos diferentes).")

    # (Opcional para adjacência): exigir quadrada
    # if linhas != colunas:
    #     raise ValueError("Matriz de adjacência deve ser quadrada.")

    diag = [matriz[i][i] for i in range(min(linhas, colunas))]
    return (linhas, colunas), diag

#Valida que é retangular; opcionalmente valida que é quadrada.
def dimensaoMatriz_flex(matriz):
    linhas = len(matriz)
    colunas = max((len(l) for l in matriz), default=0)
    diag = [linha[i] for i, linha in enumerate(matriz) if i < len(linha)]
    return (linhas, colunas), diag

