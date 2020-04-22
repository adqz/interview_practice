def delete_zero_sum_subtree(root):
    root_sum = post_order_traverse_dfs(root)
    if root_sum == 0:
        root == None
    return root

def post_order_traverse_dfs(node):
    if node is None:
        return node
    # Base
    if is_leaf(node):
        return node.data

    # Build
    sum_left = post_order_traverse_dfs(node.left)
    sum_right = post_order_traverse_dfs(node.right)
    
    if sum_left == 0:
        node.left = None
    if sum_right == 0:
        node.right = None
    
    return node.data + sum_left + sum_right

def is_leaf(node):
    if node.left is None and node.right is None:
        return True
    return False