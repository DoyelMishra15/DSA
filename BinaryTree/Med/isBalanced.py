# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))
        def check(node):
            if node is None:
                return True
            lh = height(node.left)
            rh = height(node.right)
            if abs(lh - rh) > 1:
                return False
            left = check(node.left)
            right = check(node.right)
            if not left or not right:
                return False
            return True
        return check(root)
