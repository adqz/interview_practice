'''
@author: adnan
Problem 279. Perfect Squares (Medium)

Runtime: 204 ms, faster than 82.84% of Python3 online submissions for Perfect Squares.
Memory Usage: 13.6 MB, less than 70.00% of Python3 online submissions for Perfect Squares.
'''
from typing import List
from collections import deque, defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.make_graph(equations, values)

        result_ratios = []
        for from_var, to_var in queries:
            queue = deque([[from_var, 1.0]])
            # visited = set()
            while queue:
                curr, curr_ratio = queue.popleft()
                if curr == to_var:
                    result_ratios.append(curr_ratio)
                    break
                elif curr in graph.keys():
                    next_var, next_ratio = graph[curr][0]
                    queue.append([next_var, curr_ratio*next_ratio])
                else:
                    result_ratios.append(-1)
                    break
        
        return result_ratios
                    

    def make_graph(self, equations, values):
        graph = defaultdict(list)
        for i, equation in enumerate(equations):
            a, b = equation
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))
    
        return graph


if __name__ == '__main__':
    sol = Solution()
    equations = [ ["a", "b"], ["b", "c"] ]
    values = [2.0, 3.0]
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
    print(sol.calcEquation(equations,values,queries))