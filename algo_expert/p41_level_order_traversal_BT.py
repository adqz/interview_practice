from collections import deque
def level_order_traversal(root):
    result = ""
    # 1. Make queue
    queue = deque([root])
    # 2. Iterate over queue
    while queue:
        # 3. Keep size
        size, curr_level = len(queue), ""
        
        for _ in range(size):
            node = queue.popleft()
            curr_level += str(node.data) + " "
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(curr_level[:-1])
        result += curr_level[:-1] + " "
    return result[:-1]