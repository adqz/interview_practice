'''
@author: adnan
Problem No. 39. Combination Sum (Medium)

Runtime: 988 ms, faster than 5.01% of Python3 online submissions for Combination Sum.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Combination Sum.
'''
from typing import List
class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    
    if candidates:
      self.output = []
      self.backtrack(candidates, target, [])
      return self.output
    else:
      return []

  def backtrack(self, candidates, target, combi):
    if sum(combi) == target: #base case
      combi_sorted = sorted(combi)
      if combi_sorted not in self.output: #checking for duplicates
        self.output.append(combi_sorted)
    
    elif sum(combi) > target: #base case
      return []
    
    else:
      for num in candidates:
        self.backtrack(candidates, target, combi + [num])

if __name__ == '__main__':

  sol = Solution()
  testcase, target = [2,3,6,7], 7
  ans = sol.combinationSum(testcase, target)
  print(f'ans = {ans}')

  testcase, target = [2,3,5], 8
  ans = sol.combinationSum(testcase, target)
  print(f'ans = {ans}')

'''
from typing import List
class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    
    if candidates:
      self.output = []
      self.backtrack(candidates, target, [])
      return self.output
    else:
      return []

  def backtrack(self, candidates, target, combi):
    if sum(combi) == target: #base case
      combi_sorted = sorted(combi)
      if combi_sorted not in self.output: #checking for duplicates
        self.output.append(combi_sorted)
    
    elif sum(combi) > target: #base case
      return []
    
    else:
      for num in candidates:
        self.backtrack(candidates, target, combi + [num])
'''