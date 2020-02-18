# @author: adnan
# Problem 42. Trapping Rain Water
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
  # ------ Test Cases ------
  s = Solution()
  seq1 = [2, 1, 2]
  seq2 = [3, 0, 1, 3, 0, 5]
  seq3 = [6, 7, 8, 0, 4, 6, 8, 0, 3, 5, 5, 6, 3, 0, 9]
  seq4 = [1,2,1,3]
  seq5 = [2, 1]
  seq6 = [0,1,0,2,1,0,1,3,2,1,2,1]
  assert s.trap(seq1) == 1, 'Total volume should be 1'
  assert s.trap(seq2) == 8, 'Total volume should be 8'
  assert s.trap(seq3) == 48, 'Total volume should be 48'
  assert s.trap(seq4) == 1, 'Total volume should be 1'
  assert s.trap(seq5) == 0, 'Total volume should be 0'
  assert s.trap(seq6) == 6, 'Total volume should be 6'
  print('All test cases passed!')