# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Edge case
    if descendantOne.name == descendantTwo.name:
        return descendantOne
    
    depth_descendantOne = get_depth(descendantOne, topAncestor)
    depth_descendantTwo = get_depth(descendantTwo, topAncestor)

    if depth_descendantOne > depth_descendantTwo:
        height_diff = depth_descendantOne-depth_descendantTwo
        return backtrack_to_common_ancestor(descendantOne, descendantTwo, height_diff)
    else:
        height_diff = depth_descendantTwo - depth_descendantOne
        return backtrack_to_common_ancestor(descendantTwo, descendantOne, height_diff)

def get_depth(node, root):
    depth = 0
    while node.name != root.name:
        node = node.ancestor
        depth += 1
    return depth

def backtrack_to_common_ancestor(lower_node, higher_node, height_diff):
    while height_diff > 0:
        lower_node = lower_node.ancestor
        height_diff -= 1
    
    while lower_node.name != higher_node.name:
        lower_node = lower_node.ancestor
        higher_node = higher_node.ancestor
    
    return lower_node
