# Função: contaRegressivaRecursao(numero)
# Descrição: função que recebe um número x e imprime em cada linha um número correspondente a contagem regressiva de x até o valor 1. Utilize uma estratégia de recursão.
# Entrada: matriz de adjacências.
# Saída: números inteiros.
# Por exemplo:
# Teste: contaRegressivaRecursao(10)
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

def contaRegressivaRecursao(primeiroNumeroContagem):
    if primeiroNumeroContagem == 0:
        return
    print(primeiroNumeroContagem)
    contaRegressivaRecursao(primeiroNumeroContagem - 1)


# Otimizações e cuidados
# Limite de recursão: Python não otimiza tail recursion e o limite padrão é ~1000 níveis. 
# Para n muito grande, prefira iterativo. Uma versão híbrida segura:
# def contaRegressivaRecursao_segura(n: int) -> None:
#     if n <= 0:
#         return
#     if n > 950:  # margem para evitar RecursionError
#         for i in range(n, 0, -1):
#             print(i)
#         return
#     print(n)
#     contaRegressivaRecursao_segura(n - 1)


# Outras maneiras:

# 1) Com validação e type hints (mesma lógica, mais robusta)
# def contaRegressivaRecursao(n: int) -> None:
#     if not isinstance(n, int):
#         raise TypeError("n deve ser inteiro")
#     if n <= 0:
#         return
#     print(n)
#     contaRegressivaRecursao(n - 1)

# 2) Com parâmetro de parada configurável (stop)
# def contaRegressivaRecursao_stop(n: int, stop: int = 1) -> None:
#     if n < stop:
#         return
#     print(n)
#     contaRegressivaRecursao_stop(n - 1, stop)

# 3) Usando um “estado” interno (parâmetro auxiliar)
# def contaRegressivaRecursao_aux(n: int, atual: int | None = None) -> None:
#     if atual is None:
#         atual = n
#     if atual <= 0:
#         return
#     print(atual)
#     contaRegressivaRecursao_aux(n, atual - 1)
