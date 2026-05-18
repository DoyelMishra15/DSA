from collections import deque

class Solution:
    def leftView(self, root):

        if root is None:
            return []

        q = deque([root])

        ans = []

        while q:

            size = len(q)

            for i in range(size):

                node = q.popleft()

                if i == 0:
                    ans.append(node.data)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return ans
