class BSTIterator:

    def __init__(self, root):
        self.s = []
        self.i = -1

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.s.append(node.val)
            inorder(node.right)

        inorder(root)

    def next(self):
        self.i += 1
        return self.s[self.i]

    def hasNext(self):
        return self.i + 1 < len(self.s)
