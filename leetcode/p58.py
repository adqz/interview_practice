'''
@author: adnan
Problem 206. Reverse Linked List (Easy)

Runtime: 40 ms, faster than 61.05% of Python3 online submissions for Reverse Linked List.
Memory Usage: 14.6 MB, less than 38.64% of Python3 online submissions for Reverse Linked List.
'''
from typing import List
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    if not head:
      return head
    # convert to list
    l = []
    curr_node = head
    while curr_node:
      l.append(curr_node.val)
      curr_node = curr_node.next
    # reversing 
    ans = l[::-1]
    # convert to linked list

    return self.make_linked_list(ans)
  
  def make_linked_list(self, list_elemnts):
    head = ListNode(list_elemnts[0])
    node = head
    for i in range(1, len(list_elemnts)):
      new_node = ListNode(list_elemnts[i])
      node.next = new_node
      node = new_node
    
    return head

if __name__ == '__main__':
  sol = Solution()
  head = sol.make_linked_list([7,9,8,2,3])
  ans = sol.reverseList(head)
  while ans:
    print(ans.val, '-> ', end='')
    ans = ans.next
  print('Null')