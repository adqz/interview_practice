'''
@author: adnan
Problem No. 98. Validate Binary Search Tree (Medium)

Runtime: 40 ms, faster than 96.02% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Validate Binary Search Tree.
'''
from typing import List
import tree_visualizer
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def isValidBST(self, root: TreeNode, Min=None, Max=None) -> bool:
    if root:
      if Min!=None and root.val <= Min:
        return False
      if Max!=None and root.val >= Max:
        return False

      if root.left and not(self.isValidBST(root.left, Min, root.val)):
        return False
      if root.right and not(self.isValidBST(root.right, root.val, Max)):
        return False

    return True

if __name__ == '__main__':
  sol = Solution()
  root = tree_visualizer.deserialize('[5,1,4,null,null,3,6]')
  ans = sol.isValidBST(root)
  print(f'ans = {ans}')

  root = tree_visualizer.deserialize('[2,1,3]')
  ans = sol.isValidBST(root)
  print(f'ans = {ans}')

  root = tree_visualizer.deserialize('[1,null,1]')
  ans = sol.isValidBST(root)
  print(f'ans = {ans}')
  tree_visualizer.drawtree(root)