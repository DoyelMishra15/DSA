from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = {}
        q = deque([(root, 0, 0)])
        while q:
            node, col, row = q.popleft()
            if col not in mp:
                mp[col] = []
            mp[col].append((row, node.val))
            if node.left:
                q.append((node.left, col - 1, row + 1))
            if node.right:
                q.append((node.right, col + 1, row + 1))
        ans = []
        for col in sorted(mp.keys()):
            level = sorted(mp[col])
            temp = []
            for row, val in level:
                temp.append(val)
            ans.append(temp)
        return ans
