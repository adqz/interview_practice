'''
@author: adnan
Problem No. 500. Keyboard Row (Easy)
Passed in FIRST attempt!
Runtime: 28 ms, faster than 92.73% of Python3 online submissions for Keyboard Row.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Keyboard Row.
'''

from typing import List
class Solution:
  def findWords(self, words: List[str]) -> List[str]:
    row1 = {'q','w','e','r','t','y','u','i','o','p'}
    row2 = {'a', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 's'}
    row3 = {'z','x','c','v','b','n','m'}
    ans = []
    for word in words:
      word_set = set(word.lower())
      if word_set.issubset(row1) or word_set.issubset(row2) or word_set.issubset(row3):
        ans.append(word)
    return ans

if __name__ == '__main__':

  sol = Solution()
  testcase = ["Hello", "Alaska", "Dad", "Peace"]
  ans = sol.findWords(testcase)
  print(f'ans = {ans}')