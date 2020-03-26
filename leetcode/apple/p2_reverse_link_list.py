# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
@author: adnan
Problem 206. Reverse Linked List (Easy)

Runtime: 36 ms, faster than 54.12% of Python3 online submissions for Reverse Linked List.
Memory Usage: 14.4 MB, less than 79.55% of Python3 online submissions for Reverse Linked List.
'''

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        curr_node = head
        prev_node = None
        while curr_node and curr_node.next:
            next_node = curr_node.next
            next_next_node = curr_node.next.next
            # Switching
            next_node.next = curr_node
            curr_node.next = prev_node
            prev_node = next_node
            curr_node = next_next_node
        
        if curr_node:
            curr_node.next = prev_node
            head = curr_node
        else:
            head = next_node

        return head
def generate_linked_list_from_iterable(iterable, visualize = False):
    for i, val in enumerate(iterable):
        if i == 0:
            head = ListNode(val)
            curr = head
        else:
            curr.next = ListNode(val)
            curr = curr.next
    if visualize:
        print_linked_list(head)
    
    return head

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, '-> ', end='')
        curr = curr.next
    print('None')
    
    
if __name__ == "__main__":
    sol = Solution()
    head = generate_linked_list_from_iterable(range(1,5), visualize = True)
    ans = sol.reverseList(head)
    print_linked_list(ans)
