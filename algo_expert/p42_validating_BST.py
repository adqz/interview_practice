def is_bst(root):
    
    return helper_is_bst(root, -float('inf'), float('inf'))
    
def helper_is_bst(root, min_value, max_value):
    if root is None:
        return True
    
    if root.data < min_value or root.data > max_value:
        return False
    
    return helper_is_bst(root.left, min_value, root.data) and helper_is_bst(root.right, root.data, max_value)