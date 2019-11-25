import itertools as it
from collections import defaultdict
'''
@author: adnan
Problem No. 64. Minimum Path Sum (Medium)

Runtime: 104 ms, faster than 91.05% of Python3 online submissions for Minimum Path Sum.
Memory Usage: 17.9 MB, less than 17.54% of Python3 online submissions for Minimum Path Sum.
'''
class Solution(object):
  def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    nRows = len(grid)
    nCol = len(grid[0])
    
    d = defaultdict()
    for i,j in it.product(range(nRows), range(nCol)):
      if (i,j) == (0,0): #start point
        d[0,0] = grid[0][0]
      elif i==0: #leftmost colum
        d[i,j] = grid[i][j] + d[i,j-1]
      elif j==0: #topmost row
        d[i,j] = grid[i][j] + d[i-1,j]
      else: #general case
        d[i,j] = grid[i][j] + min(d[i-1,j], d[i,j-1])
      # print(f'd[{i},{j}] = {d[i,j]}')
    return d[nRows-1, nCol-1]

if __name__ == '__main__':

  sol = Solution()
  testcase = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
  ans = sol.minPathSum(testcase)
  print(f'ans = {ans}')
