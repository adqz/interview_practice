'''
@author: adnan
Problem No. 17. Letter Combinations of a Phone Number (Medium)

Runtime: 28 ms, faster than 91.02% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Letter Combinations of a Phone Number.
'''
from typing import List
class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    digits = list(digits)
    digits = list(map(int, digits))
    self.digit_to_letters = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    }
    self.output = []
    if digits:
      self.backtrack('', digits)

    return self.output

  def backtrack(self, combi, digits):
    
    if digits:
      digit = digits[0]
      for letter in self.digit_to_letters[digit]:
        self.backtrack(combi + letter, digits[1:])
    else:
      self.output.append(combi)


if __name__ == '__main__':

  sol = Solution()
  testcase = '222'
  ans = sol.letterCombinations(testcase)
  print(f'ans = {ans}')
