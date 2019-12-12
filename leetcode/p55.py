from typing import List
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def numComponents(self, head: ListNode, G: List[int]) -> int:
    curr_node = head
    G = set(G) #remove duplicates. Makes looking up faster
    counter = 0

    while curr_node:
      if curr_node.val in G:
        if curr_node.next == None or curr_node.next.val not in G:
          # we are at the end of a component if we are either at the end or
          # the next value in the list is not there in G
          counter += 1
      curr_node = curr_node.next
    
    return counter

def sample_linked_list(m):
  head = ListNode(0)
  node = head
  for i in range(1,m+1):
    new_node = ListNode(i)
    node.next = new_node
    node = new_node
  
  return head

if __name__ == '__main__':
  
  head = sample_linked_list(3)
  # print(head.val, head.next.val, head.next.next.val, head.next.next.next.val, head.next.next.next.next.val)
  sol = Solution()
  ans = sol.numComponents(head, [0,1,3])
  print(f'ans = {ans}')
