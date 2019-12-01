'''
@author: adnan
Problem No. 637. Average of Levels in Binary Tree (Easy)

Runtime: 52 ms, faster than 83.14% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Average of Levels in Binary Tree.
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
  def averageOfLevels(self, root: TreeNode) -> List[List[int]]:
    if root == None:
      return None
    
    ans = []
    buffer = [root]
    while buffer:
      level = []
      len_buffer = len(buffer)
      for i in range(len_buffer):
        node = buffer.pop(0)
        level.append(node.val)
        if node.left != None: buffer.append(node.left)
        if node.right != None: buffer.append(node.right)
      ans.append(level)
    ans = [sum(i)/len(i) for i in ans]
    return ans

if __name__ == '__main__':
  sol = Solution()
  root = tree_visualizer.deserialize('[3,9,20,null,null,15,7]')
  ans = sol.averageOfLevels(root)
  print(ans)
