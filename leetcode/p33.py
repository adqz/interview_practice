'''
@author: adnan
Problem No. 463. Island Perimeter (Easy)

Runtime: 560 ms, faster than 77.42% of Python3 online submissions for Island Perimeter.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Island Perimeter.
'''
from itertools import product
from typing import List
class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    nR, nC = len(grid), len(grid[0])
    perimeter=0
    for i,j in product(range(nR), range(nC)):
      if grid[i][j]:
        perimeter += 4
        if i>0 and grid[i-1][j]: perimeter -= 2
        if j>0 and grid[i][j-1]: perimeter -= 2
        print('perimeter = ', perimeter)
    return perimeter

if __name__ == '__main__':

  sol = Solution()
  testcase = [[0,1,0,0],
              [1,1,1,0],
              [0,1,0,0],
              [1,1,0,0]]
  ans = sol.islandPerimeter(testcase)
  print(f'ans = {ans}')