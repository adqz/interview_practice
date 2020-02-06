'''
@author: adnan
Problem 994. Rotting Oranges (Easy)

Runtime: 48 ms, faster than 83.49% of Python3 online submissions for Rotting Oranges.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Rotting Oranges.
'''
from typing import List
from collections import deque

class Solution:
  def orangesRotting(self, grid: List[List[int]]) -> int:
    self.R = len(grid)
    self.C = len(grid[0])
    queue = deque()

    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 2:
                queue.append((r,c,0)) # 0 is the depth
    # Rotting neighbour oranges with BFS
    d = 0
    while queue:
        # 1. Get node (Pop a rotten orange)
        r, c, d = queue.popleft()
        # 2. Get children of node (neighbour oranges)
        neighbours = self.get_neighbours(r, c)
        # 3. Check each child for a condition and add to queue (make neighbor rotten and add the new rotten orange to queue)
        for nr, nc in neighbours:
            if grid[nr][nc] == 1:
                grid[nr][nc] = 2
                queue.append((nr, nc, d+1))
    
    if any([1 in row for row in grid]):
        return -1
    else:
        return d
          
    
  def get_neighbours(self, r, c):
    neighbours = []
    for nr, nc in [(r-1,c), (r+1,c), (r, c-1), (r, c+1)]:
        if (0 <= nr < self.R) and (0 <= nc < self.C):
            neighbours.append((nr, nc))
    
    return neighbours

if __name__ == '__main__':
    sol = Solution()
    ans = sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) #4
    print(ans)
    ans = sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) #-1
    print(ans)
    ans = sol.orangesRotting([[0,2]]) #0
    print(ans)