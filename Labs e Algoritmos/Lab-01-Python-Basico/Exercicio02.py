# Função: valorCelula
# Descrição: 
# imprime o elemento da posição [i][j] informado pelo usuário. 
# Informa caso algum índice dado como entrada seja maior que a dimensão da matriz.
# Entrada: matriz de adjacências
# Saída: Elemento da matriz na célula [i][j] ou mensagem de 'Erro'.
# Por exemplo:
# Teste: valorCelula([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 2, 3)
# Input: [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 2, 3
# Resultado: Celula[2][3] = 1

def valorCelula(celula, posicao_i, posicao_j):
    if posicao_i < 0 or posicao_i >= len(celula):
        return print("Erro")
    if posicao_j < 0 or posicao_j >= len(celula[0]):
        return print("Erro")
    print(f"Celula[{posicao_i}][{posicao_j}] = {celula[posicao_i][posicao_j]}")

#Verificação GPT que garantam tambem verificacao de uma matriz irregular
def valorCelula(celula, posicao_i, posicao_j):
    # matriz vazia?
    if not celula:
        print("Erro")
        return
    # checa linha
    if posicao_i < 0 or posicao_i >= len(celula):
        print("Erro")
        return
    # checa coluna usando o tamanho da linha i
    if posicao_j < 0 or posicao_j >= len(celula[posicao_i]):
        print("Erro")
        return

    print(f"Celula[{posicao_i}][{posicao_j}] = {celula[posicao_i][posicao_j]}")
