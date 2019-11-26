'''
@author: adnan
Problem No. 14. Longest Common Prefix (Easy)

Runtime: 28 ms, faster than 97.26% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.
'''
from typing import List
class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
      return ''
    i=0
    cmn_prefix = ''
    for i in range(len(min(strs))):
      if len(set([word[i] for word in strs])) == 1:
        cmn_prefix += strs[0][i]
        continue
      else:
        break
    return cmn_prefix

if __name__ == '__main__':

  sol = Solution()
  testcase = ["flower","flow","flight"]
  ans = sol.longestCommonPrefix(testcase)
  print(f'ans = {ans}')
  testcase = ["dog","racecar","car"]
  ans = sol.longestCommonPrefix(testcase)
  print(f'ans = {ans}')
  testcase = ["", 'b']
  ans = sol.longestCommonPrefix(testcase)
  print(f'ans = {ans}')
  testcase = ["a"]
  ans = sol.longestCommonPrefix(testcase)
  print(f'ans = {ans}')
  