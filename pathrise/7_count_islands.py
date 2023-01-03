#!/bin/python3

import os
import sys
from collections import deque
# Complete the function below.
'''
You are given a binary matrix as an input. You want to return the number of islands in the binary matrix.  You can think of the 0's as the ocean and the 1's as land.  An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

Examples: 

# There are 6 islands in this matrix
{1, 1, 0, 0, 0},
{0, 1, 0, 0, 1},
{1, 0, 0, 1, 1},
{0, 0, 0, 0, 0},
{1, 0, 1, 0, 1}

# There is 1 island in this matrix
{1, 1, 1, 1, 1},
{1, 1, 1, 1, 1},
{1, 1, 1, 1, 1}

[
[1,1,1,1,0],
[1,1,0,1,0],
[1,1,0,0,0],
[0,0,0,0,0]
]
'''
class Solution:
    def countIslands(self, mat):
        # Write your code here.
        '''
        for each_1 in matrix:
            find out the 1's connected to it and so on
        '''
        self.visited = set()
        self.R = len(mat)
        self.C = len(mat[0])
        island_count = 0
        
        for r in range(self.R):
            for c in range(self.C):
                if mat[r][c] == 1 and (r,c) not in self.visited:
                    # Do bfs and make an island, while marking all the 1's in the island as visited
                    # self.bfs(mat, r, c)
                    # print('Doing dfs')
                    self.dfs(mat, r, c)
                    island_count += 1
        
        return island_count
             
    def get_neighbours(self, r, c):
        neighbours = []
        for nr, nc in [(r+1, c), (r-1,c), (r, c+1), (r,c-1)]:
            if 0 <= nr < self.R and 0 <= nc < self.C:
                neighbours.append([nr, nc])
        return neighbours
    
    def bfs(self, mat, r, c):
        queue = deque([[r, c]])
        while queue:
            # 1. Pop element from queue
            r, c = queue.popleft()
            self.visited.add((r,c))
            neighbours = self.get_neighbours(r,c)
            # 2. Going through neighbours
            for neighbour in neighbours:
                nr, nc = neighbour
                if mat[nr][nc] == 1 and (nr, nc) not in self.visited:
                    queue.append([nr,nc])
    
    def dfs(self, mat, r, c):
        # print('r,c = ', r,c)
        if 0 <= r < self.R and 0 <= c < self.C:
            # Base
            if mat[r][c] == 1 and (r,c) not in self.visited:
                self.visited.add((r,c))
                # Build
                self.dfs(mat, r+1, c) # move down
                self.dfs(mat, r-1, c) # move up
                self.dfs(mat, r, c+1) # move right
                self.dfs(mat, r, c-1) # move left
            
            

if __name__ == "__main__":
    sol = Solution()
    island1 = [ [1,1,1,1,0], 
                [1,1,0,1,0],
                [1,1,0,0,0],
                [0,0,0,0,0] ]
    print(sol.countIslands(island1)) #1
    island2 =   [[1, 1, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [1, 0, 0, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1]]
    print(sol.countIslands(island2)) #6
    island3 = [ [1,0,0],
                [1,0,1] ]
    print(sol.countIslands(island3)) #2


    # [   [x,1,1,1,0], 
    #     [x,1,0,1,0],
    #     [x,x,0,0,0],
    #     [0,0,0,0,0] ]