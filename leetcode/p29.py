'''
@author: adnan
Problem No. 392. Is Subsequence (Easy)

Runtime: 16 ms, faster than 98.68% of Python online submissions for Is Subsequence.
Memory Usage: 19 MB, less than 75.00% of Python online submissions for Is Subsequence.
'''
class Solution(object):
  def isSubsequence(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    for i in range(len(s)):
      try:
        index = t.index(s[i]) #get index of occurence of character
      except ValueError:
        return False #if character is not there, then return False
      t = t[index+1:] #chop off left side because order matters
    return True

if __name__ == '__main__':

  sol = Solution()
  s, t = 'abc', 'ahbgdc'
  ans = sol.isSubsequence(s,t)
  print(f'ans = {ans}')