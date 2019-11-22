'''
Runtime: 84 ms, faster than 26.42% of Python online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 13.6 MB, less than 64.06% of Python online submissions for Remove Duplicates from Sorted Array.
'''
class Solution(object):
  def removeDuplicates(self, nums):
    """
    Orig thought: Two pointer solution where i is slow and j is fast. j starts at i+1 and keeps incrementing
    until nums[i] != nums[j]. if this happens, we delete all duplicates except the one at the jth position.
    Corner cases include when arr is of length 0 or 1 and when j goes outside the array.
    
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) in [0,1]: #corner case 1: only 1 or 0 elements in array
      nums = len(nums)
      return nums
    
    i,j = 0,1 # slow and fast pointers
    while True:
      if j == len(nums): #corner case 2: when j goes outside the array index so we cut it off
        del nums[i:j-1]
        break
      if nums[i] != nums[j]: #main case
        del nums[i:j-1]
        i += 1
        j = i+1
      else:
        j += 1
    nums = len(nums)
    return nums

if __name__ == '__main__':

  s = Solution()
  testcase = [1, 1, 2, 2, 2]
  ans = s.removeDuplicates(testcase)
  print(f'ans = {ans}')
  testcase = [1, 1, 2]
  ans = s.removeDuplicates(testcase)
  print(f'ans = {ans}')
  testcase = [1, 1, 2, 2, 3]
  ans = s.removeDuplicates(testcase)
  print(f'ans = {ans}')
  testcase = [1, 2, 3, 4]
  ans = s.removeDuplicates(testcase)
  print(f'ans = {ans}')
  testcase = [1, 2]
  ans = s.removeDuplicates(testcase)
  print(f'ans = {ans}')
  testcase = [1]
  ans = s.removeDuplicates(testcase)
  print(f'ans = {ans}')
  testcase = [0,0,1,1,1,2,2,3,3,4]
  ans = s.removeDuplicates(testcase)
  print(f'ans = {ans}')
  testcase = [0]
  ans = s.removeDuplicates(testcase)
  print(f'ans = {ans}')
  testcase = []
  ans = s.removeDuplicates(testcase)
  print(f'ans = {ans}')