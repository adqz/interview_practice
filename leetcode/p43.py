'''
@author: adnan
Problem No. 104. Maximum Depth of Binary Tree (Easy)

Runtime: 40 ms, faster than 90.98% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 14.4 MB, less than 96.87% of Python3 online submissions for Maximum Depth of Binary Tree.
'''
from typing import List
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

def makeTree(nodes):
  '''
  if parent node is at index i in the array then the left child of that 
  node is at index (2*i + 1) and right child is at index (2*i + 2) in the array
  '''
  i = 0
  n = TreeNode(nodes[i])
  parent = n
  while True:
    try:
      parent.left = TreeNode(nodes[2*i + 1])
      parent.right = TreeNode(nodes[2*i + 2])
    except IndexError:
      break
    i += 1
    if i%2 == 0:
      parent = parent.right
    else:
      parent = parent.left

  return n

class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    if root == None:
      return 0
    
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)
    return max(left, right) + 1
    

if __name__ == '__main__':
  sol = Solution()
  root = [1,2,3,4]
  n = makeTree(root)
  ans = sol.maxDepth(n)
  print(f'ans = {ans}')