class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        all_nodes = {value: Node(value) for value in range(1, n+1)}
        self.visited = set()
        self.count = 0
        for root_value in range(1, n+1):
            root = Node(root_value)
            # self.visited.add(root_value)
            self.make_BST_dfs(root, all_nodes)
            self.visited.remove(root_value)

        return self.count

    def make_BST_dfs(self, curr_node, all_nodes):
        # Base
        self.visited.add(curr_node.value)
        print(curr_node.value, end = ', ')
        if len(self.visited) == len(all_nodes):
            self.count += 1
            print()
            return
        
        # Build
        for node_value, node in all_nodes.items():
            if node_value not in self.visited:
                if node_value < curr_node.value:
                    curr_node.left = node
                elif node_value > curr_node.value:
                    curr_node.right = node
                self.make_BST_dfs(node, all_nodes)
                self.visited.remove(node_value)

if __name__ == "__main__":
    sol = Solution()
    # print(sol.numTrees(1)) #1
    # print(sol.numTrees(2)) #2
    print(sol.numTrees(3)) #5