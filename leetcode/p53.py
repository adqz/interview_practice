from typing import List
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    #  Calculate left array
    L = [1]*len(nums)
    R = [1]*len(nums)
    ans = [0]*len(nums)
    for i in range(1, len(nums)):
      L[i] = L[i-1] * nums[i-1]
    
    for i in reversed(range(len(nums)-1)):
      R[i] = R[i+1]*nums[i+1]
    
    for i in range(0, len(nums)):
      ans[i] = L[i] * R[i]

    return ans

if __name__ == '__main__':
  sol = Solution()
  ans = sol.productExceptSelf([1,2,3,4])
  print(f'ans = {ans}')

'''
import numpy as np
from typing import List
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    if not(nums):
      return []
    ans = []
    for i in range(len(nums)):
      ans.append(np.prod(nums[0:i]+nums[i+1:]))
    return ans
'''