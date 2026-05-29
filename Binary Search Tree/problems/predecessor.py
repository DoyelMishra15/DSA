def predecessor(root, key):
    ans = None

    while root:
        if key > root.val:
            ans = root
            root = root.right
        else:
            root = root.left

    return ans
