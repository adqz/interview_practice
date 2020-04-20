from collections import deque

def populate_sibling_pointers(root):
    levels = bfs(root)
    for level in levels:
        for i in range(len(level)-1):
            level[i].next = level[i+1]
    
    return root

def bfs(root):
    levels = []
    # 1. Make queue
    queue = deque([root])
    # 2. Iterate over queue
    while queue:
        # 3. Keep size
        curr_level, size = [], len(queue)
        # 4. Expand children
        for _ in range(size):
            node = queue.popleft()
            curr_level.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(curr_level)
    
    return levels
        