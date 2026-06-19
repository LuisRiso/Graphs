# Função: removeVértice(listaAdj, vi)

# Descrição: Remove um vértice do grafo.

# Entrada: lista de adjacências

# Saída: lista de adjacências sem o vértice.


def removeVerticeLista(listaAdj, vi):

    for vertices in listaAdj.values():
        while vi in vertices:
            vertices.remove(vi)

    listaAdj.pop(vi, None)

    print(listaAdj)


#Outro modo
# 1) Ajuste mínimo (só corrigindo seu código)
# Remove todas as ocorrências de vi em cada lista e depois remove a chave vi:
def removeVerticeLista(listaAdj, vi):
    for adj in listaAdj.values():           
        while True:
            try:
                adj.remove(vi)              
            except ValueError:
                break                       
    listaAdj.pop(vi, None)                  
    print(listaAdj)

#Outro modo
# 2) Versão linear (mais limpa/rápida)
# Usa list comprehension para tirar todas as ocorrências de vi de uma vez:
def removeVerticeLista(listaAdj, vi):
    for u in list(listaAdj):                # copia das chaves para evitar surpresas
        if u != vi:
            listaAdj[u] = [x for x in listaAdj[u] if x != vi]
    listaAdj.pop(vi, None)
    print(listaAdj)


# Quando otimizar ainda mais
# Se o grafo for não dirigido e você quiser evitar varrer tudo, dá pra tocar só nos vizinhos de vi (complexidade menor quando o grau de vi é pequeno):
def removeVerticeLista_undirected(listaAdj, vi):
    vizinhos = set(listaAdj.pop(vi, []))
    for u in vizinhos:
        if u in listaAdj:
            listaAdj[u] = [x for x in listaAdj[u] if x != vi]


