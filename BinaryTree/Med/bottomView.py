from collections import deque

class Solution:
    def bottomView(self, root):

        if root is None:
            return []

        mp = {}

        q = deque([(root, 0)])

        while q:

            node, col = q.popleft()

            mp[col] = node.data

            if node.left:
                q.append((node.left, col - 1))

            if node.right:
                q.append((node.right, col + 1))

        ans = []

        for col in sorted(mp.keys()):
            ans.append(mp[col])

        return ans
