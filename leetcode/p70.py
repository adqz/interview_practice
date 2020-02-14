'''
@author: adnan
Problem 684. Redundant Connection (Medium)
'''
from collections import defaultdict
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.graph = self.make_adjacency_list(edges)
        self.visited = set()
        self.extra_edges = []
        for node in self.graph.keys():
            if node not in self.visited:
                self.dfs(node, None)
        
        return self.extra_edges
    
    def dfs(self, curr_node, parent_node):
        children = self.graph[curr_node]
        self.visited.add(curr_node)
        for child in children:
            if child in self.visited and child != parent_node and parent_node != None:
                self.extra_edges.append([child, curr_node])
            if child not in self.visited:
                self.dfs(child, curr_node)
    
    def make_adjacency_list(self, edge_list):
        graph = defaultdict(list)
        for node1, node2 in edge_list:
            graph[node1].append(node2)
            graph[node2].append(node1)
        return graph

if __name__ == "__main__":
    sol = Solution()
    # print(sol.findRedundantConnection([[1,2], [1,3], [2,3]]))
    # print(sol.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
    print(sol.findRedundantConnection([[0,1], [0,2], [2,3], [2,4], [3,4]]))