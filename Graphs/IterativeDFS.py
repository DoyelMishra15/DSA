def dfs(start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            print(node)

            for nei in graph[node]:
                if nei not in visited:
                    stack.append(nei)
