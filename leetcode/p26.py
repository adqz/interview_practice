'''
@author: adnan
Problem No. 189. Rotate Array (Easy)

Runtime: 140 ms, faster than 15.10% of Python online submissions for Rotate Array.
Memory Usage: 12.1 MB, less than 62.50% of Python online submissions for Rotate Array.
FIRST ATTEMPT! :D
'''
class Solution(object):
  def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    for _ in range(k):
      nums.insert(0, nums.pop())
    return nums

if __name__ == '__main__':

  s = Solution()
  testcase, k = [1,2,3,4,5,6,7], 1
  ans = s.rotate(testcase, k)
  print(f'ans = {ans}')
  testcase, k = [1,2,3,4,5,6,7], 3
  ans = s.rotate(testcase, k)
  print(f'ans = {ans}')
  testcase, k = [1,2,3,4,5,6,7], len(testcase)
  ans = s.rotate(testcase, k)
  print(f'ans = {ans}')