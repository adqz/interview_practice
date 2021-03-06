'''
@author: adnan
Problem 206. Reverse Linked List (Easy)

Runtime: 28 ms, faster than 97.39% of Python3 online submissions for Reverse Linked List.
Memory Usage: 17.3 MB, less than 22.73% of Python3 online submissions for Reverse Linked List.
'''
from typing import List
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    curr = head
    if curr == None or curr.next == None: # base case
      return curr
  
    p = self.reverseList(curr.next)
    curr.next.next = curr
    curr.next = None

    return p

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

'''
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
'''