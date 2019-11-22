'''
Runtime: 12 ms, faster than 97.05% of Python online submissions for Remove Element.
Memory Usage: 11.8 MB, less than 32.08% of Python online submissions for Remove Element.
'''
class Solution(object):
  def removeElement(self, nums, val):
    '''
    Orig Thought: Go through each element and delete if it matches val. There are 2 corner cases.
    1st is empty list whose solution is trivial.
    2nd is when the pointer is at the last value, we remove it if its equal to val and break the loop 
    else just break the loop.

    :type nums: list
    :type val: int
    :rtype: int
    '''
    if len(nums) == 0: #corner case 1: empty list
      nums = len(nums)
      return nums
    i = 0
    while True:
      if i == len(nums)-1: #corner case 2: at the end of the list
        if val == nums[i]:
          del nums[i]
          break
        else:
          break
      if val == nums[i]: #main case
        del nums[i]
      else:
        i+=1
    nums = len(nums)
    return nums

if __name__ == '__main__':

  s = Solution()
  testcase, val = [1, 1, 2, 2, 2], 1
  ans = s.removeElement(testcase, val)
  print(f'ans = {ans}')
  testcase, val = [1, 1, 2, 2], 2
  ans = s.removeElement(testcase, val)
  print(f'ans = {ans}')
  testcase, val = [1], 1
  ans = s.removeElement(testcase, val)
  print(f'ans = {ans}')
  testcase, val = [1], 2
  ans = s.removeElement(testcase, val)
  print(f'ans = {ans}')
  testcase, val = [], 2
  ans = s.removeElement(testcase, val)
  print(f'ans = {ans}')