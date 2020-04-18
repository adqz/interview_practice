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

def merge_sort(head):
    if not head or not head.next:
        return head
    
    # Split in two halves using fast/slow pointer method
    head1 = head
    # Setting slow pointer
    slow = head
    # Setting fast pointer 
    if head.next and head.next.next:
        fast = head.next.next
    if head.next:
        fast = head.next
    # Moving fast and slow pointer
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # Setting head2 to next node after slow
    head2 = slow.next
    slow.next = None

    return merge(merge_sort(head1), merge_sort(head2))

def merge(head1, head2):
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
    head = generate_linked_list_from_iterable([], True)
    ans = merge_sort(head)
    print_linked_list(ans)
    print()
    head = generate_linked_list_from_iterable([5], True)
    ans = merge_sort(head)
    print_linked_list(ans)
    print()
    head = generate_linked_list_from_iterable([5,2], True)
    ans = merge_sort(head)
    print_linked_list(ans)
    print()
    head = generate_linked_list_from_iterable([5,11,23,29,82], True)
    ans = merge_sort(head)
    print_linked_list(ans)
    print()
    head = generate_linked_list_from_iterable([29,23,82,11,5], True)
    ans = merge_sort(head)
    print_linked_list(ans)
    print()