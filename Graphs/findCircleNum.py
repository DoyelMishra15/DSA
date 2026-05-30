class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vis=set()
        def dfs(node):
            vis.add(node)
            for nei in range(len(isConnected)):
                if isConnected[node][nei] == 1 and nei not in vis:
                    dfs(nei)
        tot=0
        for node in range(len(isConnected)):
            if node not in vis:
                dfs(node)
                tot+=1
        return tot
