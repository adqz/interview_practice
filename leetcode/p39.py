'''
@author: adnan
Problem No. 78. Subsets (Medium)

Runtime: 32 ms, faster than 92.86% of Python3 online submissions for Subsets.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Subsets.
'''
from typing import List
class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    if len(nums) == 0:
      return []
    
    return self.partition(nums,[],0)
  
  def partition(self, nums, subset, index):
    if index == len(nums):
      return [subset]
    elif index > len(nums):
      return []
    else:
      return self.partition(nums, subset, index+1) + self.partition(nums, subset + [nums[index]], index+1)

if __name__ == '__main__':

  sol = Solution()
  testcase = [1,2,3]
  ans = sol.subsets(testcase)
  print(f'ans = {ans}')
  testcase = []
  ans = sol.subsets(testcase)
  print(f'ans = {ans}')
  testcase = [1]
  ans = sol.subsets(testcase)
  print(f'ans = {ans}')
  testcase = [1,4,5,7]
  ans = sol.subsets(testcase)
  print(f'len(ans), ans = {len(ans), ans}')