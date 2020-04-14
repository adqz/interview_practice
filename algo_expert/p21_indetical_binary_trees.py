# O(n) time | O(h) space, n = number of nodes, h = height. Space is O(h) due to recursion stack
def are_identical(root1, root2):

    # Base case
    if root1 is None and root2 is None:
        return True
    
    # General case
    if root1 == root2:
        left = are_identical(root1.left, root2.left)
        right = are_identical(root1.right, root2.right)
        return (root1.data == root2.data) and left and right

    return False