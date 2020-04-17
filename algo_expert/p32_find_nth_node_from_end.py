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

def find_nth_from_last(head, n):
    
    # 1. Set slow and fast pointer at index 0 and n in linked list
    slow = head
    counter = 0
    while head and head.next and counter < n:
        head = head.next
        counter += 1
    # Edge Case: If length of linked list is < n
    if counter < n:
        return None
    else:
        fast = head

    # 2. Move slow and fast until fast reaches last node. Return slow at this point as it is n nodes away
    while fast != None:
        fast = fast.next
        slow = slow.next

    return slow

if __name__ == "__main__":
    head = generate_linked_list_from_iterable([1,4,2], True)
    ans = find_nth_from_last(head, 1)
    print(ans.data)
    print()
    head = generate_linked_list_from_iterable([4,1,4,2], True)
    ans = find_nth_from_last(head, 2)
    print(ans.data)
    print()
    head = generate_linked_list_from_iterable([1,2,3,4,5,6], True)
    ans = find_nth_from_last(head, 4)
    print(ans.data)
    print()