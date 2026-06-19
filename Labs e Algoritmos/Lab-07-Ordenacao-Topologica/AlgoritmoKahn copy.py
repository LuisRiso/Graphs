from collections import deque

# We mainly take input graph as a set of edges. This function is
# mainly a utility function to convert the edges to an adjacency
# list
def constructadj(V, edges):
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
    return adj

# Function to return list containing vertices in Topological order
def topologicalSort(V, edges):
    adj = constructadj(V, edges)
    indegree = [0] * V

    # Calculate indegree of each vertex
    for u in range(V):
        for v in adj[u]:
            indegree[v] += 1

    # Queue to store vertices with indegree 0
    q = deque([i for i in range(V) if indegree[i] == 0])
    
    result = []
    while q:
        node = q.popleft()
        result.append(node)

        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    # Check for cycle
    if len(result) != V:
        print("Graph contains cycle!")
        return []

    return result

if __name__ == "__main__":
    V = 9
    edges = [[0, 1], [0, 3], [1, 2], [3, 2], [5, 6], [6, 3], [6, 7], [8, 7]]

    result = topologicalSort(V, edges)
    if result:
        print("Topological Order:", result)



lista1 = {0: [1], 1: [], 2: [0], 3: [1, 2], 4: [1, 2]}
lista2 = {0: [1, 3], 1: [2], 2: [], 3: [2], 4: [], 5: [6, 7], 6: [3, 7], 7: [], 8: [7]}
lista3 = {0: [1, 3, 5], 1: [2], 2: [3, 4], 3: [], 4: [6], 5: [4, 6], 6: [7, 8], 7: [8], 8: [], 9: [6]}
lista4 = {0:[1,2], 1:[3], 2:[3], 3:[]}
#ordenacaoTopologicaKahn(lista1)
#ordenacaoTopologicaKahn(lista2)
#ordenacaoTopologicaKahn(lista3)
#ordenacaoTopologicaKahn(lista4)

