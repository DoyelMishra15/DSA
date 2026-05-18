# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float('-inf')
        def maxPath(node):
            if node is None:
                return 0
            leftSum = max(0, maxPath(node.left))
            rightSum = max(0, maxPath(node.right))
            self.maxi = max(self.maxi,leftSum + rightSum + node.val)
            return node.val + max(leftSum, rightSum)
        maxPath(root)
        return self.maxi
