# Função: contaRegressivaWhile(numero)
# Descrição: função que recebe um número x e imprime em cada linha um número correspondente a contagem regressiva de x até o valor 1. Utilize o comando While.
# Entrada: matriz de adjacências.
# Saída: números inteiros.
# Por exemplo:
# Teste: contaRegressivaWhile(10)
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

def contaRegressivaWhile(primeiroNumeroContagem):
    while primeiroNumeroContagem > 0:
        print(primeiroNumeroContagem)
        primeiroNumeroContagem -= 1

# outras maneiras

# def contaRegressivaWhile1(numero):
#     n = numero
#     while n > 0:
#         print(n)
#         n -= 1

# def contaRegressivaWhile2(numero):
#     while True:
#         print(numero)
#         numero -= 1
#         if numero == 0:
#             break

# def contaRegressivaWhile3(numero):
#     i = 1
#     while i <= numero:
#         print(numero - i + 1)
#         i += 1
