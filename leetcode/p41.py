'''
@author: adnan
Problem No. 350. Intersection of Two Arrays II (Easy)

Runtime: 40 ms, faster than 98.71% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays II.
'''
from collections import Counter
from typing import List
class Solution:
  def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
    count1 = Counter(nums1)
    intersection = []
    for num in nums2:
      if count1[num] > 0:
        count1[num] -= 1
        intersection.append(num)
    return intersection

if __name__ == '__main__':
  sol = Solution()
  nums1 = [1,2,2,1]
  nums2 = [2,2]
  ans = sol.intersect(nums1, nums2)
  print(f'ans = {ans}')
  
  nums1 = [4,9,5]
  nums2 = [9,4,9,8,4]
  ans = sol.intersect(nums1, nums2)
  print(f'ans = {ans}')

  nums1 = []
  nums2 = []
  ans = sol.intersect(nums1, nums2)
  print(f'ans = {ans}')