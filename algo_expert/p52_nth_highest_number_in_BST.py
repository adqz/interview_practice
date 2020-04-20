current_n = 0
def find_nth_highest_in_bst(node, n):
    if not node:
        return None
    global current_n
    current_n = 0
    return reverse_in_order_traversal(node, n)

def reverse_in_order_traversal(node, desired_n):
    if node is None:
        return None
    # Right
    ans = reverse_in_order_traversal(node.right, desired_n)
    if ans is not None:
        return ans
    # Visit
    global current_n
    current_n = current_n + 1
    print('current_n, node.data = ', current_n, node.data)
    if desired_n == current_n:
        return node
    # Left
    ans = reverse_in_order_traversal(node.left, desired_n)
    if ans is not None:
        return ans

    return None