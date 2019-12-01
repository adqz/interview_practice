'''
@author: adnan
Problem No. 108. Convert Sorted Array to Binary Search Tree (Easy)

Runtime: 60 ms, faster than 98.88% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Convert Sorted Array to Binary Search Tree
'''
from typing import List
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if not nums:
      return None
    
    return self.constructBST(nums, 0, len(nums)-1)
  
  def constructBST(self, nums, left, right):
    if left > right:
      return None

    mid = left + (right-left)//2
    current_node = TreeNode(nums[mid])
    current_node.left = self.constructBST(nums, left, mid-1)
    current_node.right = self.constructBST(nums, mid+1, right)

    return current_node

def printBST(root):
  buffer = [root]
  last_seen = root.val
  prev_buffer_len = len(buffer)
  print(last_seen)
  while buffer:
    node = buffer.pop(0)
    if node.left != None:
      buffer += [node.left]
    if node.right != None:
      buffer += [node.right]  
    if len(buffer) > prev_buffer_len:
      prev_buffer_len = len(buffer)
      if buffer[0].val != last_seen:
        for el in buffer:
          print(el.val, ' ', end='')
          last_seen = el.val
        print()
    
    
  

if __name__ == '__main__':
  sol = Solution()
  nums = [0,1,2,3,4,5,6,7,8]
  ans = sol.sortedArrayToBST(nums)
  printBST(ans)
  # print(f'ans = {ans}')

'''
class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if not nums:
      return None
    middle = nums.pop(len(nums)//2)
    root = TreeNode(middle)
    while nums:
      to_insert = nums.pop()
      self.insert(root, to_insert)
    return root
  
  def insert(self, node, to_insert):
    if node.left != None and to_insert < node.val:
      self.insert(node.left, to_insert)
    elif to_insert < node.val:
      node.left = TreeNode(to_insert)
    elif node.right != None and to_insert > node.val:
      self.insert(node.right, to_insert)
    elif to_insert > node.val:
      node.right = TreeNode(to_insert)
'''