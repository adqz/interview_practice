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

def reverse_even_nodes(head):
    # Edge case
    if not head: return head

    prev_slow = head
    if head.next and head.next.next and head.next.next.next:
        slow      = head.next
        prev_fast = head.next.next
        fast      = head.next.next.next
    else:
        return head
    # Swap slow with fast
    prev_slow.next = fast
    prev_fast.next = slow
    slow.next = fast.next
    fast.next = prev_fast
    # Rename after swap
    fast = slow
    slow = prev_slow.next

    while fast.next and fast.next.next:
        prev_slow = prev_slow.next.next
        slow = slow.next.next
        prev_fast = prev_fast.next.next
        fast = fast.next.next
        
        # Swap slow with fast
        prev_slow.next = fast
        prev_fast.next = slow
        slow.next = fast.next
        fast.next = prev_fast
        # Rename after swap
        fast = slow
        slow = prev_slow.next

    return head

if __name__ == "__main__":
    head = generate_linked_list_from_iterable([7,14,21], True)
    ans = reverse_even_nodes(head)
    print_linked_list(ans)
    print()
    head = generate_linked_list_from_iterable([7,14,21,28], True)
    ans = reverse_even_nodes(head)
    print_linked_list(ans)
    print()
    head = generate_linked_list_from_iterable([7,14,21,28,9], True)
    ans = reverse_even_nodes(head)
    print_linked_list(ans)
    print()
    head = generate_linked_list_from_iterable([7,14,21,28,9,20,21,50,9], True)
    ans = reverse_even_nodes(head)
    print_linked_list(ans)
    print()