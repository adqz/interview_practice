'''
@author: adnan
Problem No. 746. Min Cost Climbing Stairs (Easy)

Runtime: 40 ms, faster than 80.76% of Python online submissions for Min Cost Climbing Stairs.
Memory Usage: 12 MB, less than 14.29% of Python online submissions for Min Cost Climbing Stairs.
'''
from collections import defaultdict
class Solution(object):
  def minCostClimbingStairs(self, cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    d = defaultdict()
    cost.append(0) #adding goal node which has zero cost to be at
    for i in range(len(cost)):
      if i in [0,1]:
        d[i] = cost[i]
      else:
        d[i] = cost[i] + min(d[i-1], d[i-2])
    return d[len(cost)-1]

if __name__ == '__main__':

  sol = Solution()
  testcase = [10,15,20]
  ans = sol.minCostClimbingStairs(testcase)
  print(f'ans = {ans}')
  testcase = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
  ans = sol.minCostClimbingStairs(testcase)
  print(f'ans = {ans}')

'''
from collections import defaultdict
class Solution(object):
  def minCostClimbingStairs(self, cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    d = defaultdict()
    cost.append(0) #adding goal node which has zero cost to be at
    for i in range(len(cost)):
      if i in [0,1]:
        d[i] = lambda i: cost[i]
      else:
        d[i] = lambda i: cost[i] + min(d[i-1](i-1), d[i-2](i-2))
    return d[len(cost)-1](len(cost)-1)
'''

'''
class Solution(object):
  def minCostClimbingStairs(self, cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    d = defaultdict()
    cost.append(0) #adding goal node which has zero cost to be at
    for i in range(len(cost)):
      if i in [0,1]:
        d[i] = cost[i]
      else:
        d[i] = cost[i] + min(d[i-1], d[i-2])
    return d[len(cost)-1]
'''