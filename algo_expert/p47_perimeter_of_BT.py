def display_tree_perimeter(root):
    result = ""
    left_perimeter, right_perimeter = "", ""
    visited = set()

    # Part 1: Left perimeter
    node = root
    while node:
        left_perimeter += str(node.data) + " "
        visited.add(node.data)
        node = node.left
    # Part 2: Right perimeter
    node = root.right
    while node:
        right_perimeter = str(node.data) + " " + right_perimeter
        visited.add(node.data)
        node = node.right
    # Part 3: Bottom perimeter
    node = root
    bottom_perimeter = [] #Can't make it a string because strings are immutable so every time 
    # we add something to it, it becomes a new object with a new address. So we make a list 
    # and then join all its elements as a string
    dfs(node, visited, bottom_perimeter)
    bottom_perimeter = ' '.join(bottom_perimeter) + ' '
    
    result = left_perimeter + bottom_perimeter + right_perimeter
    return result

def dfs(node, visited, bottom_perimeter):
    # Base
    if node.left is None and node.right is None and node.data not in visited:
        bottom_perimeter.append(str(node.data))
        visited.add(node.data)
    # Build
    if node.left:
        dfs(node.left, visited, bottom_perimeter)
    if node.right:
        dfs(node.right, visited, bottom_perimeter)