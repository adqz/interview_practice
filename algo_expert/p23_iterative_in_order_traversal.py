# O(n) time | O(h) space, where h is height of binary tree
def inorder_iterative(root):
    result = ""
    stack = []
    node = root
    while len(stack) != 0 or node != None:
        if node != None:
            stack.append(node)
            node = node.left
            continue
        
        curr_node = stack.pop()
        result += str(curr_node.data) + " "
        node = curr_node.right
    return result