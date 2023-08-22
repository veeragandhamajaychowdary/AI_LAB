def dfs(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

num_vertices = int(input())
num_edges = int(input())
graph = {}
for i in range(num_vertices):
    graph[i] = []

for _ in range(num_edges):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start_vertex = int(input())
visited = set()
dfs(graph, start_vertex, visited)
