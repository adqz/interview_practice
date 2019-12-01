'''
@author: adnan
Problem No. 429. N-ary Tree Level Order Traversal (Medium)

Runtime: 52 ms, faster than 98.55% of Python3 online submissions for N-ary Tree Level Order Traversal.
Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for N-ary Tree Level Order Traversal.
'''
from typing import List
# Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children

class Solution:
  def levelOrder(self, root: 'Node') -> List[List[int]]:
    if root == None:
      return []
    buffer = [root,'s']
    ans = []
    level = []
    while True:
      node = buffer.pop(0)
      if node == 's':
        ans.append(level)
        if len(buffer) == 0:
          break
        buffer.append(node)
        level = []
      else:
        level.append(node.val)
        if node.children:
          buffer += node.children

    return ans