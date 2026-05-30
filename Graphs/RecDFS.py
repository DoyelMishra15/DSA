graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

visited = set()

def dfs(node):
    visited.add(node)
    print(node)

    for nei in graph[node]:
        if nei not in visited:
            dfs(nei)

dfs(0)
