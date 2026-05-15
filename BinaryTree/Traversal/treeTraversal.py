# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeTraversal(self, root: Optional[TreeNode]):
        if not root:
            return [], [], []

        pre = []
        inorder = []
        post = []

        stack = [(root, 1)]

        while stack:
            node, state = stack.pop()

            if state == 1:
                pre.append(node.val)
                stack.append((node, 2))

                if node.left:
                    stack.append((node.left, 1))

            elif state == 2:
                inorder.append(node.val)
                stack.append((node, 3))

                if node.right:
                    stack.append((node.right, 1))

            else:
                post.append(node.val)

        return pre, inorder, post
