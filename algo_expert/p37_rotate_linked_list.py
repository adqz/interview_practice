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

def rotate_list(head, n):
    if not head: return head

    length = get_length(head)
    n = n % length #normalizing n with length
    if n == 0:
        return head
        
    slow = head
    
    fast = head
    for _ in range(n):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next
    
    new_head = slow.next
    slow.next = None
    fast.next = head
    
    return new_head

def get_length(head):
    if not head:
        return 0
    
    counter = 0
    while head:
        counter += 1
        head = head.next
    
    return counter

if __name__ == "__main__":
    head = generate_linked_list_from_iterable([1,2,3,4,5], True)
    ans = rotate_list(head,2)
    print_linked_list(ans)
    print()
    head = generate_linked_list_from_iterable([1,2,3,4,5], True)
    ans = rotate_list(head,7)
    print_linked_list(ans)
    print()