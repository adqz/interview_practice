def inorder_successor_bst(root, d, parent=None, parent_of_parent=None):
    if not root:
        return None
    
    if d == root.data and root.right:
        return root.right
    elif d == root.data and d < parent.data:
        return parent
    elif d == root.data and d > parent.data:
        return parent_of_parent
    
    elif d < root.data:
        return inorder_successor_bst(root.left, d, root, parent)
    elif d > root.data:
        return inorder_successor_bst(root.right, d, root, parent)
    