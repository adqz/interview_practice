from collections import deque

def populate_sibling_pointers(root):
    levels = bfs(root)
    for level_index, curr_level in enumerate(levels):
        # connecting nodes at current level
        for node_index in range(len(curr_level)-1):
            curr_level[node_index].next = curr_level[node_index+1]
        # connecting last node of current level to first node of next level
        if level_index < len(levels)-1:
            curr_level[-1].next = levels[level_index+1][0]
    
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
        