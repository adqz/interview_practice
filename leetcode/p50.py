'''
@author: adnan
Problem No. 501. Find Mode in Binary Search Tree (Easy)

Runtime: 52 ms, faster than 96.42% of Python3 online submissions for Find Mode in Binary Search Tree.
Memory Usage: 16.7 MB, less than 100.00% of Python3 online submissions for Find Mode in Binary Search Tree.
'''
from typing import List
from collections import defaultdict
import tree_visualizer
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def findMode(self, root: TreeNode) -> List[int]:
    if not(root):
      return []
    
    counter = defaultdict(int)
    counter = self.countValues(root, counter)
    max_freq = max(counter.values())
    
    ans = [key for key, val in counter.items() if val == max_freq]
    return ans

  def countValues(self, node, counter):
    if node:
      counter[node.val] += 1
      counter = self.countValues(node.left, counter)
      counter = self.countValues(node.right, counter)
    return counter

if __name__ == '__main__':
  sol = Solution()
  root = tree_visualizer.deserialize('[0]')
  ans = sol.findMode(root)
  print(f'ans = {ans}')