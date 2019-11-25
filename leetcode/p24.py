'''
@author: adnan
Problem No. 42 - Trapping Rain Water (Hard)

Runtime: 56 ms, faster than 82.91% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 13.4 MB, less than 97.67% of Python3 online submissions for Trapping Rain Water.
'''
from typing import List
class Solution:
  def trap(self, height: List[int]) -> int:
    max_left = list([0])
    max_right = list([0])
    for i in range(len(height)):
      max_left.append(max(max_left[-1], height[i]))
      max_right.append(max(max_right[-1], height[len(height)-i-1]))
    max_left = max_left[1:]
    max_right = max_right[1:][::-1]
    
    totalWater = 0
    for i in range(len(height)):
      totalWater += min(max_left[i], max_right[i]) - height[i]
    return totalWater


if __name__ == '__main__':

  sol = Solution()
  testcase = [0,1,0,2,1,0,1,3,2,1,2,1]
  ans = sol.trap(testcase)
  print(f'ans = {ans}')
