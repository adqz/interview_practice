def mirror_tree(root):
    if not root:
        return None
    
    mirror_tree(root.left)
    mirror_tree(root.right)
    
    temp = root.left
    root.left = root.right
    root.right = temp

    return root