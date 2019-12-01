'''
@author: adnan
Problem No. 589. N-ary Tree Preorder Traversal (Easy)

Runtime: 44 ms, faster than 99.21% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for N-ary Tree Preorder Traversal.
'''
from typing import List
# Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children

class Solution:
  def preorder(self, root: 'Node') -> List[List[int]]:
    if root == None:
      return []
    buffer = [root]
    ans = []
    while buffer:
      node = buffer.pop(0)
      ans.append(node.val)
      if node.children:
        buffer = node.children + buffer

    return ans