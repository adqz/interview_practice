def inorder_iterative(root):
    in_order_stack = []
    stack = []
    node = root
    while len(stack) != 0 or node != None:
        if node != None:
            stack.append(node)
            node = node.left
            continue
        
        curr_node = stack.pop()
        in_order_stack.append(curr_node.data)
        node = curr_node.right

    result = ' '.join(map(in_order_stack, str))
    return result