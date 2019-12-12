'''
@author: adnan
Problem 92. Reverse Linked List II (Meidum)

Runtime: 28 ms, faster than 89.97% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Linked List II.
'''
from typing import List
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    # convert to list
    l = []
    curr_node = head
    while curr_node:
      l.append(curr_node.val)
      curr_node = curr_node.next
    # reversing from m to n
    m, n = m-1, n-1 # adjust for 0 indexing
    ans = l[0:m] + l[m:n+1][::-1] + l[n+1:]
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
  ans = sol.reverseBetween(head, 2, 4)
  while ans:
    print(ans.val, '-> ', end='')
    ans = ans.next
  print('Null')