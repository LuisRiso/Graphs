# Função: contaRegressivaFor(numero)
# Descrição: função que recebe um número x e imprime em cada linha um número correspondente a contagem regressiva de x até o valor 1. Utilize o comando for.
# Entrada: matriz de adjacências.
# Saída: números inteiros.
# Por exemplo:
# Teste: contaRegressivaFor(10)	
# Input: 10
# Resultado:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1


def contaRegressivaFor(primeiroNumeroContagem):
    for n in range(primeiroNumeroContagem, 0, -1):
        print(n)

# outras maneiras

# def contaRegressivaFor2(numero):
#     for n in list(range(numero, 0, -1)):
#         print(n)

# def contaRegressivaFor3(numero):
#     for n in reversed(range(1, numero + 1)):
#         print(n)


