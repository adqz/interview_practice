'''
@author: adnan
Problem No. 560. Subarray Sum Equals K (Medium)

Runtime: 116 ms, faster than 91.49% of Python3 online submissions for Subarray Sum Equals K.
Memory Usage: 15.2 MB, less than 96.00% of Python3 online submissions for Subarray Sum Equals K.
'''
from typing import List
from collections import defaultdict
class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    if len(nums) == 0:
      return 0
    sums = defaultdict(int) #key is the cumulative sum and value is number of times it occured
    cum_sum, count = 0, 0
    sums[cum_sum] = 1 # Initialization: The cumulation sum 0 has occured once
    for i in range(len(nums)):
      cum_sum += nums[i]
      if ((cum_sum-k) in sums.keys()):
        count += sums[cum_sum-k] #increase count by number of times it was seen
      sums[cum_sum] += 1 #IMP: add to dictionary after checking!
    # print(sums)
    return count

if __name__ == '__main__':

  sol = Solution()

  testcase, k = [3,4,7,2,-3,1,4,2], 7
  ans = sol.subarraySum(testcase, k)
  print(f'ans = {ans}')

  testcase, k = [1,1,1], 2
  ans = sol.subarraySum(testcase, k)
  print(f'ans = {ans}')

  testcase, k = [1,1,1,3,1,1,2], 2
  ans = sol.subarraySum(testcase, k)
  print(f'ans = {ans}')

  testcase, k = [-1,-1,1], 0
  ans = sol.subarraySum(testcase, k)
  print(f'ans = {ans}')

  testcase, k = [0,0,0,0,0,0,0,0,0,0], 0
  ans = sol.subarraySum(testcase, k)
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
'''
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
'''