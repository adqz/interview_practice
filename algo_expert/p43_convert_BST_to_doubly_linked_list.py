def convert_to_linked_list(root):
    in_order_list = in_order_traversal(root)
    return convert_list_to_doubly_linked_list(in_order_list)

def in_order_traversal(root):
    if root is None:
        return None
    
    result = []
    node = root
    stack = []
    while len(stack) != 0 or node is not None:
        if node is not None:
            stack.append(node)
            node = node.left

        curr_node = stack.pop()
        result.append(curr_node)
        node = curr_node.right
    return result

def convert_list_to_doubly_linked_list(l):
    # TODO
    pass