'''
@author: adnan
Problem 554. Brick Wall (Medium)

Runtime: 180 ms, faster than 98.09% of Python3 online submissions for Brick Wall.
Memory Usage: 17.5 MB, less than 50.00% of Python3 online submissions for Brick Wall.
'''
from typing import List
from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # 1. Find number of common edges in all rows
        common_edges = defaultdict(int)
        for row in wall:
            curr_width = 0
            for brick in row[:-1]: #not including last brick
                curr_width += brick
                common_edges[curr_width] += 1
        # 2. Find max number of rows with a certain common edge and subtract it from height of wall
        max_common_edges = max(list(common_edges.values()) + [0])
        min_bricks_crossed = len(wall) - max_common_edges
        
        return min_bricks_crossed

if __name__ == '__main__':
    sol = Solution()
    ans = sol.leastBricks([[1,2,2,1],
                    [3,1,2],
                    [1,3,2],
                    [2,4],
                    [3,1,2],
                    [1,3,1,1]])
    print(ans) #2
    ans = sol.leastBricks([[1], [1], [1]])
    print(ans) #1


'''
# Solution 1: Brute force. Fails for certain cases
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        total_wall_width = sum(wall[0])
        
        wall = [w[::-1] for w in wall]
        curr_wall_width = dict()
        for i, row in enumerate(wall):
            curr_wall_width[i] = row.pop()
        
        min_bricks_crossed = float('inf')
        for curr_index in range(1,total_wall_width):
            num_bricks_crossed = 0
            
            for row, row_width in curr_wall_width.items():
                # Updating 
                if curr_index == row_width:
                    curr_wall_width[row] += wall[row].pop()
                if curr_index < row_width:
                    num_bricks_crossed += 1
            if num_bricks_crossed < min_bricks_crossed:
                min_bricks_crossed = num_bricks_crossed
        
        return min_bricks_crossed
'''