
from typing import List
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    if not head or head.next == None:
      return None
    l = []
    while head:
      l.append(head)
      head = head.next
    try:
      l[-n-1].next = l[-n+1]
    except IndexError:
      pass
    l[-n].next = None

    return l[0]
  
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
  head = sol.make_linked_list(list(range(1,3)))
  ans = sol.removeNthFromEnd(head, 2)
  while ans:
    print(ans.val, '-> ', end='')
    ans = ans.next
  print('Null')