'''
@author: adnan
Problem No. 198. House Robber (Easy)

Runtime: 24 ms, faster than 98.53% of Python3 online submissions for House Robber.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for House Robber.
'''
from typing import List
from collections import defaultdict
class Solution:
  def rob(self, nums: List[int]) -> int:
    if len(nums) == 0:
      return 0
    if len(nums) in [1,2]:
      return max(nums)
    
    house = defaultdict(int)
    house[0], house[1] = nums[0], max(nums[0], nums[1])
    for i in range(2,len(nums)):
      house[i] = max(house[i-1], house[i-2] + nums[i])
    
    return house[len(nums)-1]

if __name__ == '__main__':
  sol = Solution()
  testcase = [1,2,3,1]
  ans = sol.rob(testcase)
  print(f'ans = {ans}')
  testcase = [2,7,9,3,1]
  ans = sol.rob(testcase)
  print(f'ans = {ans}')
  testcase = [1,10,1,0,0,100]
  ans = sol.rob(testcase)
  print(f'ans = {ans}')