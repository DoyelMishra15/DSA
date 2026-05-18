from collections import deque

class Solution:
    def rightSideView(self, root):
        if root is None:
            return []
        q = deque([root])
        ans = []
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == size - 1:
                    ans.append(node.val)
        return ans
