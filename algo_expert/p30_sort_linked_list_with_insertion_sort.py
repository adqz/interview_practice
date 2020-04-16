class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def generate_linked_list_from_iterable(iterable, visualize = False):
    if not iterable:
        return None
    
    for i, val in enumerate(iterable):
        if i == 0:
            head = Node(val)
            curr = head
        else:
            curr.next = Node(val)
            curr = curr.next
    if visualize:
        print_linked_list(head)
    
    return head

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data, '-> ', end='')
        curr = curr.next
    print('None')

def helper_insertion_sort(head, node):
    if not node:
        return head
    # Case 1: node is less than head, so node should be head
    if head is None or  node.data <= head.data:
        node.next = head
        return node
    
    # Case 2: node is not less than head, so keep going to next node until node > next
    curr = head
    while curr.next and curr.next.data <= node.data:
        curr = curr.next
    # Switch curr with node next > node
    node.next = curr.next
    curr.next = node

    return head

# O(n^2) time | O(1) space
def insertion_sort(head):
    # Edge case
    if not head or head.next == None:
        return head

    new_head = None
    curr = head

    while curr:
        temp = curr.next
        new_head = helper_insertion_sort(new_head, curr)
        curr = temp

    return new_head

if __name__ == "__main__":
    # head = generate_linked_list_from_iterable([], True)
    # ans = insertion_sort(head)
    # print_linked_list(ans)
    # print()

    # head = generate_linked_list_from_iterable([2], True)
    # ans = insertion_sort(head)
    # print_linked_list(ans)
    # print()

    head = generate_linked_list_from_iterable([2,4,7,3], True)
    ans = insertion_sort(head)
    print_linked_list(ans)
    print()