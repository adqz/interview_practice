from collections import defaultdict
class Node:
    def __init__(self, d):
        self.data = d
        self.neighbors = []

def clone(root):
    # Make adjacency list using DFS
    graph_adjacency_list = defaultdict(list)
    visited = set()
    get_adjacency_list_dfs(root, graph_adjacency_list, visited)
    # Make new root node
    new_root = Node(root.data)
    # Make new graph using DFS
    all_nodes = {value: Node(value) for value in graph_adjacency_list.keys()}
    visited = set()
    create_graph_from_adjacency_list_dfs(new_root, graph_adjacency_list, all_nodes, visited)

    return root

def get_adjacency_list_dfs(node, graph, visited):
    # Base
    if node.data in visited:
        return
    # Build
    visited.add(node.data)
    for neighbour in node.neighbors:
        graph[node.data].append(neighbour.data)
        get_adjacency_list_dfs(neighbour, graph, visited)
    
    return

def create_graph_from_adjacency_list_dfs(node, graph, all_nodes, visited):
    if node.data in visited:
        return
    
    visited.add(node.data)
    for neighbour_value in graph[node.data]:
        neighbour = all_nodes[neighbour_value]
        node.neighbors.append(neighbour)
        create_graph_from_adjacency_list_dfs(neighbour, graph, all_nodes, visited)
    
    return
            