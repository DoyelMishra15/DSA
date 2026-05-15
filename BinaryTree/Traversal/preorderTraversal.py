# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def preorder(node):
            if not node:
                return
            
            ans.append(node.val)   # Root
            preorder(node.left)   # Left
            preorder(node.right)  # Right

        preorder(root)
        return ans
