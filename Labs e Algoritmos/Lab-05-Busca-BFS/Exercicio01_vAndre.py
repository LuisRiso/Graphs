def BFS(listaAdj, v):
    # Define listas de vértices
    vertices = []
    queue = []
    analisados = []

    # Preenche a lista de vértices com cada vértice na lista de adjacência
    for item in listaAdj:
        vertices.append(item)

    # Remove o vértice v da lista e coloca ele na fila
    vertices.remove(v)
    queue.insert(0, v)
    
    while queue or vertices:
        # Remove o vértice v da lista e coloca ele na fila
        # caso a fila esteja vazia
        # Essa condição só é satisfeita se o grafo for desconexo
        if not queue:
            v = vertices.pop(0)
            queue.insert(0,v)

        # Remove o primeiro elemento da fila
        v = queue.pop(0)

        # Para cada elemento adjacente do elemento v
        for adjacente in listaAdj[v]:
            if adjacente not in queue and adjacente not in analisados:
                # Se o elemento não for visitado ou analisado, insere na fila
                vertices.remove(adjacente)
                queue.append(adjacente)
        
        # Adiciona o vértice à lista de vértices analisados
        analisados.append(v)

    print(analisados)

lista = {0: [1, 3, 4], 
         1: [0, 2], 
         2: [1], 
         3: [0], 
         4: [0, 5], 
         5: [4]}

lista2 = {0: [2, 4], 
          1: [2, 4], 
          2: [0, 1, 4], 
          3: [], 
          4: [0, 1, 2, 5, 6], 
          5: [4, 6], 
          6: [4, 5]}

BFS(lista2, 0)
