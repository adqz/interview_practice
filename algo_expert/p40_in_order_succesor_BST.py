def inorder_successor_bst(root, d, successor=None):
    if not root:
        return None
    
    if root.data == d and root.right:
        return root.right
    if root.data == d:
        return successor
    elif d < root.data:
        return inorder_successor_bst(root.left, d, root.data)
    elif d > root.data:
        return inorder_successor_bst(root.right, d, successor)