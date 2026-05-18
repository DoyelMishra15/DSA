class Solution:
    def floorInBST(self, root, x):

        floor = -1

        while root:

            if root.val == x:
                return root.val

            if root.val < x:
                floor = root.val
                root = root.right

            else:
                root = root.left

        return floor
