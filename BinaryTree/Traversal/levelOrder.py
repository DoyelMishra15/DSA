class Solution:
    def levelOrder(self, root):

        if not root:
            return []

        q = [root]

        ans = []

        while q:

            node = q.pop(0)

            ans.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return ans
