'''
@author: adnan
Problem No. 209. Minimum Size Subarray Sum (Medium)

Runtime: 60 ms, faster than 59.77% of Python online submissions for Minimum Size Subarray Sum.
Memory Usage: 14.1 MB, less than 5.26% of Python online submissions for Minimum Size Subarray Sum.
'''

class Solution(object):
  def minSubArrayLen(self, s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    if not len(nums):
      return 0
    
    left, sums = 0, 0
    ans, soln_exist = len(nums), False
    for i in range(len(nums)):
      sums += nums[i]
      while sums >= s:
        soln_exist = True
        ans = min(ans, i-left+1)
        sums -= nums[left]
        left += 1
    return soln_exist*ans
        

if __name__ == '__main__':

  sol = Solution()
  testcase, s = [2,3,1,2,4,3], 99
  ans = sol.minSubArrayLen(s, testcase)
  print(f'ans = {ans}')
  testcase, s = [2,3,1,2,4,3], 7
  ans = sol.minSubArrayLen(s, testcase)
  print(f'ans = {ans}')
  testcase, s = [2,3,1,2,4,3], 4
  ans = sol.minSubArrayLen(s, testcase)
  print(f'ans = {ans}')
  testcase, s = [], 4
  ans = sol.minSubArrayLen(s, testcase)
  print(f'ans = {ans}')
  testcase, s = [1,2,3,4,5], 11
  ans = sol.minSubArrayLen(s, testcase)
  print(f'ans = {ans}')
  testcase, s = [1,4,4], 4
  ans = sol.minSubArrayLen(s, testcase)
  print(f'ans = {ans}')

'''
class Solution(object):
  def minSubArrayLen(self, s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    i, j = 0, 0
    min_len = len(nums)
    soln_exist = False
    while j<len(nums):
      num_sum = sum(nums[i:j+1])
      if num_sum >= s:
        soln_exist = True
        curr_interval_len = j-i+1
        i += 1
        j = i*1
        if curr_interval_len < min_len:
          min_len = curr_interval_len
      else:
        j += 1
    return soln_exist*min_len
'''