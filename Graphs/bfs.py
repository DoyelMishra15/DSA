from collections import deque

def bfs(start):
    q = deque([start])
    visited = {start}

    while q:
        node = q.popleft()
        print(node)

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
