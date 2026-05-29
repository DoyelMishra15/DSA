# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(lower,higher,root):
            if root is None:
                return True
            if lower<root.val<higher:
                return rec(lower,root.val,root.left) and rec(root.val,higher,root.right)
            else:
                return False
        return rec(-2**31-1,2**31,root)
