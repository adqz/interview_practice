'''
@author: adnan
Problem No. 554. Brick Wall (Medium)

Runtime: 180 ms, faster than 99.09% of Python3 online submissions for Brick Wall.
Memory Usage: 17.8 MB, less than 50.00% of Python3 online submissions for Brick Wall.
'''
from typing import List
from collections import defaultdict
class Solution:
  def leastBricks(self, wall: List[List[int]]) -> int:
    common_edges = defaultdict(int)
    for line in wall:
      width = 0
      for brick in line[:-1]:
        width += brick
        common_edges[width] += 1
    for k,v in common_edges.items():
      print(k,v)
    num_common_edges = list(common_edges.values()) + [0]
    min_bricks_crossed = len(wall) - max(num_common_edges)
    return min_bricks_crossed

if __name__ == '__main__':

  sol = Solution()
  testcase = [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]
  ans = sol.leastBricks(testcase)
  print(f'ans = {ans}')