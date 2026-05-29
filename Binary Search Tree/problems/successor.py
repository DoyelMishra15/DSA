def successor(root, key):
    ans = None

    while root:
        if key < root.val:
            ans = root
            root = root.left
        else:
            root = root.right

    return ans
