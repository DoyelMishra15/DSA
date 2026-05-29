# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        i=0
        j=len(arr)-1
        while i<j:
            if arr[i]+arr[j]==k:
                return True
            elif arr[i]+arr[j]<k:
                i+=1
            else:
                j-=1
        return False
