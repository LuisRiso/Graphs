#Jeitos de printar
nome = "Ana"; idade = 21
# 1) f-string (recomendado)
print(f"{nome} tem {idade} anos")
# 2) Vários argumentos (print converte e separa)
print(nome, "tem", idade, "anos")
# 3) str.format
print("{} tem {} anos".format(nome, idade))
# 4) %-format (legado)
print("%s tem %d anos" % (nome, idade))
# 5) Concatenação (cuidado: precisa de str())
print(nome + " tem " + str(idade) + " anos")

#Controle de separador e fim de linha
a, b, c = 1, 2, 3
print(a, b, c, sep=" - ")      # 1 - 2 - 3
print("Sem quebra no fim", end=" ... ")
print("agora quebrou")

#Números: casas decimais, porcentagem, milhares
pi = 3.14159265; n = 1234567; taxa = 0.087
print(f"{pi:.2f}")       # 3.14
print(f"{taxa:.1%}")     # 8.7%
print(f"{n:,}")          # 1,234,567 (padrão US)
# Para espaço entre milhares:
print(f"{n:_}")          # 1_234_567

#Alinhamento, largura e preenchimento
valor = 42
print(f"|{valor:>5}|")    # direita, largura 5: |   42|
print(f"|{valor:<5}|")    # esquerda:          |42   |
print(f"|{valor:^5}|")    # centro:            | 42  |
print(f"|{valor:0>5}|")   # preenchido com 0:  |00042|

#Representações úteis (debug)
obj = {"x": 1, "y": [2,3]}
print(f"{obj!r}")     # repr (útil em debug)
x = 10
print(f"{x=}")        # Python 3.8+: x=10

#Listas: espaço entre itens / formato customizado
lst = [5,4,3,2,1]
# 1) Desempacotar (com espaço padrão)
print(*lst)                       # 5 4 3 2 1
# 2) Separador customizado
print(*lst, sep=" - ")            # 5 - 4 - 3 - 2 - 1
# 3) “Estilo enunciado”: [5 4 3 2 1]
print("[" + " ".join(map(str, lst)) + "]")

#Multilinha
nome, curso = "Ana", "Engenharia"
print(f"""Aluno: {nome}
Curso: {curso}""")

#Datas (format)
from datetime import datetime
agora = datetime(2025, 8, 18, 13, 5)
print(agora.strftime("%d/%m/%Y %H:%M"))  # 18/08/2025 13:05

#JSON bonitinho (útil para dicionários)
import json
data = {"nome": "Ana", "itens": [1,2,3]}
print(json.dumps(data, ensure_ascii=False, indent=2))

#Envio para stderr ou arquivo (quando precisar)
import sys
print("mensagem de erro", file=sys.stderr)

with open("out.txt", "w", encoding="utf-8") as f:
    print("linha no arquivo", file=f)



