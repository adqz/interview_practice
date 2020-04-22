def delete_zero_sum_subtree(root):
    post_order_traverse_dfs(root, None, dir='None')
    return root

def post_order_traverse_dfs(node, parent, dir):
    if node is None:
        return node
    # Base
    if is_leaf(node):
        return node.data

    # Build
    value_left, value_right = 0, 0
    if node.left:
        value_left = post_order_traverse_dfs(node.left, node, dir='left')
    if node.right:
        value_right = post_order_traverse_dfs(node.right, node, dir='right')
    
    subtree_sum = node.data + value_left + value_right
    if subtree_sum == 0:
        if dir == 'left':
            parent.left = None
        elif dir == 'right':
            parent.right = None
    
    return subtree_sum

def is_leaf(node):
    if node.left is None and node.right is None:
        return True
    return False