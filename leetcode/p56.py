'''
@author: adnan
Problem 445. Add Two Numbers II (Meidum)

Runtime: 76 ms, faster than 73.02% of Python3 online submissions for Add Two Numbers II.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Two Numbers II.
'''
from typing import List
# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    num1, num2 = [], []
    while l1 or l2:
      if l1:
        num1.append(l1.val)
        l1 = l1.next
      if l2:
        num2.append(l2.val)
        l2 = l2.next
    
    num1, num2 = self.list_to_int(num1), self.list_to_int(num2)
    ans = [int(x) for x in str(num1+num2)][::-1] #reversing so we can pop from end instead of beginning
    
    # Converting answer to linked list
    ans_head = ListNode(ans.pop())
    node = ans_head
    while ans:
      node.next = ListNode(ans.pop())
      node = node.next
    return ans_head

  def list_to_int(self, l):
    return int(''.join(map(str,l)))

def make_linked_list(list_elemnts):
  head = ListNode(list_elemnts[0])
  node = head
  for i in range(1, len(list_elemnts)):
    new_node = ListNode(list_elemnts[i])
    node.next = new_node
    node = new_node
  
  return head

if __name__ == '__main__':
  sol = Solution()
  ll1 = make_linked_list([7,1,1])
  ll2 = make_linked_list([4,4,4])
  # print(ll1.val, ll1.next.val, ll1.next.next.val, ll1.next.next.next.val)
  ans = sol.addTwoNumbers(ll1, ll2)
  # print(ans)
  while ans:
    print(ans.val, '-> ', end='')
    ans = ans.next
  print('Null')