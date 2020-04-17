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

def swap_nth_node(head, n):
    
    # 1. Set slow and fast pointer at index 0 and n in linked list
    main_head = head
    curr, prev = head, None
    counter = 0
    while counter < n:
        prev = curr
        curr = curr.next
        counter += 1
    
    if curr == None:
        return main_head
    
    # 3. Swap node after slow with head
    prev.next = main_head
    temp = main_head.next
    main_head.next = curr.next
    curr.next = temp

    return curr

if __name__ == "__main__":
    head = generate_linked_list_from_iterable([1,4,2], True)
    ans = swap_nth_node(head, 1)
    print_linked_list(ans)
    print()
    # head = generate_linked_list_from_iterable([10,1,4,2,3,6,7,4,5], True)
    # ans = swap_nth_node(head, 2)
    # print_linked_list(ans)
    # print()