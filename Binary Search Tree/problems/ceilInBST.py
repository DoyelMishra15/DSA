class Solution:
    def ceilInBST(self, root, x):

        ceil = -1

        while root:

            if root.val == x:
                return root.val

            if root.val > x:
                ceil = root.val
                root = root.left

            else:
                root = root.right

        return ceil
