from typing import List
from collections import defaultdict
class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    if len(nums) == 0:
      return 0
    
    count = 0
    for i in range(len(nums)):
      cum_sum = 0
      for j in range(i,len(nums)):
        cum_sum += nums[j]
        if cum_sum == k:
          count += 1
        
    return count

if __name__ == '__main__':

  sol = Solution()
  testcase, k = [1,1,1], 2
  ans = sol.subarraySum(testcase, 2)
  print(f'ans = {ans}')

  testcase, k = [1,1,1,3,1,1,2], 2
  ans = sol.subarraySum(testcase, 2)
  print(f'ans = {ans}')

  testcase, k = [-1,-1,1], 0
  ans = sol.subarraySum(testcase, 2)
  print(f'ans = {ans}')

'''
from typing import List
from collections import defaultdict
class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    if len(nums) == 0:
      return 0
    
    count = 0
    for i in range(len(nums)):
      for j in range(i,len(nums)):
        if sum(nums[i:j+1]) == k:
          # print(i, j+1, sum(nums[i:j+1]))
          count += 1
    return count
'''