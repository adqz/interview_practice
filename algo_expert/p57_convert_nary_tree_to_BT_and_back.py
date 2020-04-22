from collections import deque
def convert_n_ary_to_binary(node):
    root_BT = bfs_traversal(node, direction = +1)
    return root_BT

def bfs_traversal(node, direction):
    '''
    direction = +1 ---> go left
    direction = -1 ---> go right
    '''
    root = node
    queue = deque([node])

    while queue:
        node = queue.popleft()
        for child in node.children:
            child = bfs_traversal(child, direction*-1)
            if direction == 1:
                node.left = child
                node = node.left
            else:
                node.right = child
                node = node.right

    return root