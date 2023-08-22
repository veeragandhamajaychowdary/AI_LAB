def topological_sort(graph):
    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
        result.append(vertex)

    visited = set()
    result = []

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return result[::-1]

num_vertices = int(input())
num_edges = int(input())

graph = {}
for i in range(1, num_vertices + 1):
    graph[i] = []

for _ in range(num_edges):
    u, v = map(int, input().split())
    graph[u].append(v)

topological_order = topological_sort(graph)
print("Topological sorting:", topological_order)
