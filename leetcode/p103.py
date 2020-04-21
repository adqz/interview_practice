'''
@author: adnan
Problem 743. Network Delay Time (Medium)

Runtime: 9084 ms, faster than 5.02% of Python3 online submissions for Network Delay Time.
Memory Usage: 15.8 MB, less than 7.69% of Python3 online submissions for Network Delay Time.
'''
from typing import List
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        self.graph = self.get_adjacency_list_from_edge_list(times)
        self.node_time = {node: float('inf') for node in range(1,N+1)}
        self.dfs(K, 0)

        max_time = max(self.node_time.values())
        if max_time < float('inf'):
            return max_time
        else:
            return -1

    def dfs(self, node, current_time):
        # Base (no point exploring node if we've reached it in lesser time)
        if self.node_time[node] <= current_time:
            return
        
        self.node_time[node] = current_time
        # Build
        for child, time in self.graph[node]:
            self.dfs(child, current_time + time)


    def get_adjacency_list_from_edge_list(self, times):
        graph = defaultdict(list)
        for time in times:
            parent, child, weight = time
            graph[parent].append((child, weight))
        
        return graph