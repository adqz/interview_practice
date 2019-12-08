'''
@author: adnan
Problem 876. Middle of the Linked List (Easy)

Runtime: 28 ms, faster than 86.50% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Middle of the Linked List.
'''
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def middleNode(self, head: ListNode) -> ListNode:
    self.head = head
    list_size = self.size()
    node = head
    i = 0
    while i != list_size//2:
      node = node.next
      i += 1
    return node

  def size(self):
    counter = 0
    node = self.head
    while(node):
      counter += 1
      node = node.next

    return counter

def sample_linked_list(m):
  head = ListNode(1)
  node = head
  for i in range(2,m+1):
    new_node = ListNode(i)
    node.next = new_node
    node = new_node
  
  return head

if __name__ == '__main__':
  
  head = sample_linked_list(3)
  # print(head.val, head.next.val, head.next.next.val, head.next.next.next.val, head.next.next.next.next.val)
  sol = Solution()
  ans = sol.middleNode(head)
  print(f'ans = {ans.val}')
