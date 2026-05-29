class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)

        def build(preorder, inorder):
            if not preorder:
                return None

            root = TreeNode(preorder[0])

            idx = inorder.index(preorder[0])

            root.left = build(preorder[1:idx+1], inorder[:idx])
            root.right = build(preorder[idx+1:], inorder[idx+1:])

            return root

        return build(preorder, inorder)
