from collections import deque

class Solution:
    def isCycle(self, V, adj):
        vis = [False] * V

        def bfs(start):
            q = deque()
            q.append((start, -1))
            vis[start] = True

            while q:
                node, parent = q.popleft()

                for nei in adj[node]:
                    if not vis[nei]:
                        vis[nei] = True
                        q.append((nei, node))

                    elif nei != parent:
                        return True

            return False

        for i in range(V):
            if not vis[i]:
                if bfs(i):
                    return True

        return False
