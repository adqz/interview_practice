'''
@author: adnan
Problem No. 102. Binary Tree Level Order Traversal (Medium)

Runtime: 32 ms, faster than 92.82% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.
'''
from typing import List
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
    return ans

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

if __name__ == '__main__':
  sol = Solution()
  root = deserialize('[3,9,20,null,null,15,7]')
  ans = sol.levelOrder(root)
  print(ans)
