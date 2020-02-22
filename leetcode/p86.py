'''
@author: adnan
Problem 695. Max Area of Island (Medium)

Runtime: 176 ms, faster than 19.03% of Python3 online submissions for Max Area of Island.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Max Area of Island.
'''
from typing import List
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        self.seen = set()
        max_area = 0
        
        for r in range(self.R):
            for c in range(self.C):
                if grid[r][c] == 1 and (r,c) not in self.seen:
                    area = self.bfs(r, c, grid)
                    if area > max_area:
                        max_area = area
        
        return max_area

    def bfs(self, r, c, grid):
        queue = deque([(r,c)])
        self.seen.add((r,c))
        area = 0
        while queue:
            r, c = queue.popleft()
            print(r,c)
            area += 1
            neighbours = self.get_neighbours(r, c)
            
            for neighbour in neighbours:
                nr, nc = neighbour
                if grid[nr][nc] == 1 and (nr, nc) not in self.seen:
                    self.seen.add((nr, nc))
                    queue.append((nr, nc))
        return area
    
    def get_neighbours(self, r, c):
        neighbours = []
        for nr, nc in [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]:
            if 0 <= nr < self.R and 0 <= nc < self.C:
                neighbours.append((nr ,nc))
        return neighbours

if __name__ == "__main__":
    sol = Solution()
    # print(sol.maxAreaOfIsland([[0,0,0,0,0,0,0,0]])) #0
    # print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
    #                         [0,0,0,0,0,0,0,1,1,1,0,0,0],
    #                         [0,1,1,0,1,0,0,0,0,0,0,0,0],
    #                         [0,1,0,0,1,1,0,0,1,0,1,0,0],
    #                         [0,1,0,0,1,1,0,0,1,1,1,0,0],
    #                         [0,0,0,0,0,0,0,0,0,0,1,0,0],
    #                         [0,0,0,0,0,0,0,1,1,1,0,0,0],
    #                         [0,0,0,0,0,0,0,1,1,0,0,0,0]])) #0 
    print(sol.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])) #4                         