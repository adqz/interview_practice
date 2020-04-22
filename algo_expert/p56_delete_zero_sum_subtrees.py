def delete_zero_sum_subtree(root1):
    root2 = create_tree_dfs(root1)
    root3 = remove_zerosum_subtrees(root2, root1)

    return root3
def remove_zerosum_subtrees(node, original_tree):
    # Base
    if node is None:
        return node

    if node.left and node.left.data == 0:
        original_tree.left = None
        return remove_zerosum_subtrees(node.right, original_tree.right)

    if node.right and node.right.data == 0:
        original_tree.right = None
        return remove_zerosum_subtrees(node.left, original_tree.left)
    
    return original_tree

def create_tree_dfs(node):
    # Base
    if is_leaf(node):
        return node

    # Build
    if node.left:
        left_node = create_tree_dfs(node.left)
    if node.right:
        right_node = create_tree_dfs(node.right)
    # Overwrite current nodes value
    if left_node and right_node:
        node.data += left_node.data + right_node.data
    elif left_node:
        node.data += left_node.data
    elif right_node:
        node.data += right_node.data

    return node

def is_leaf(node):
    if node.left is None and node.right is None:
        return True
    return False