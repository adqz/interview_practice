# @author: adnan
# Problem No. 451. Sort Characters By Frequency (Medium)
'''
Runtime: 28 ms, faster than 95.97% of Python online submissions for Sort Characters By Frequency.
Memory Usage: 14.4 MB, less than 38.89% of Python online submissions for Sort Characters By Frequency.
'''
class Solution(object):
  def frequencySort(self, s):
    """
    :type s: str
    :rtype: str
    """
    count = dict()
    for char in s:
      try:
        count[char] += 1
      except KeyError:
        count[char] = 1
    ans = sorted(count, key=(lambda k: count[k]), reverse=True)
    ans = ''.join([char*count[char] for char in ans])
    return ans


if __name__ == '__main__':
  s = Solution()
  str1 = "tree"
  s.frequencySort(str1)
