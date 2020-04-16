# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.

# O(V+E) time | O(V) space, where V,E = number of vertices and edges
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        
        def helper_dfs(node, visited, array):
            if node is None:
                return
            
            array.append(node.name)
            visited.add(node)

            for child in node.children:
                if child not in visited:
                    helper_dfs(child, visited, array)
            return
        
        visited = set()
        array = []
        helper_dfs(self, visited, array)
        return array
                
