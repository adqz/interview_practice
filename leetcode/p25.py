'''
@author: adnan
Problem No. 167. Two Sum II - Input array is sorted (Easy)

Runtime: 48 ms, faster than 72.49% of Python online submissions for Two Sum II - Input array is sorted.
Memory Usage: 12 MB, less than 45.45% of Python online submissions for Two Sum II - Input array is sorted.
FIRST ATTEMPT! :D
'''

class Solution(object):
  def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    i, j = 0, len(numbers)-1
    while True:
      sum_nums = numbers[i] + numbers[j]
      if sum_nums == target:
        break
      elif sum_nums > target:
        j -= 1
      else:
        i += 1
    return [i+1, j+1]

if __name__ == '__main__':

  s = Solution()
  testcase, target = [2,7,11,15], 26
  ans = s.twoSum(testcase, target)
  print(f'ans = {ans}')