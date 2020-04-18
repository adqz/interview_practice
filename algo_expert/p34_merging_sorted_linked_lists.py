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

def merge_sorted(head1, head2):
    # Edge cases
    if not head1:
        return head2
    if not head2:
        return head1
    # Setting head node
    if head1.data < head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next
    
    # Iterating over both lists and comparing elements
    node = head
    while head1 and head2:
        if head1.data < head2.data:
            node.next = head1
            head1 = head1.next
        else:
            node.next = head2
            head2 = head2.next
        node = node.next
    # Adding leftover elements from linked list 1 if any
    if head1:
        node.next = head1
    # Adding leftover elements from linked list 2 if any
    if head2:
        node.next = head2
    
    return head

if __name__ == "__main__":
    head1 = generate_linked_list_from_iterable([], True)
    head2 = generate_linked_list_from_iterable([7,9,10], True)
    ans = merge_sorted(head1, head2)
    print_linked_list(ans)
    print()
    head1 = generate_linked_list_from_iterable([4,8,15], True)
    head2 = generate_linked_list_from_iterable([], True)
    ans = merge_sorted(head1, head2)
    print_linked_list(ans)
    print()
    head1 = generate_linked_list_from_iterable([4,8,15], True)
    head2 = generate_linked_list_from_iterable([7,9,10], True)
    ans = merge_sorted(head1, head2)
    print_linked_list(ans)
    print()