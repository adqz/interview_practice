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

def add_integers(integer1, integer2):
    place = 1
    ans = None
    carry = 0
    while integer1 and integer2:
        curr_num = integer1.data + integer2.data + carry
        carry = curr_num // 10
        curr_num = curr_num % 10
        ans += curr_num*place
        place *= 10
        
        integer1 = integer1.next
        integer2 = integer2.next
    
    while integer1:
        curr_num = integer1.data + carry
        carry = curr_num // 10
        curr_num = curr_num % 10
        ans += curr_num*place
        place *= 10
        integer1 = integer1.next

    while integer2:
        curr_num = integer2.data + carry
        carry = curr_num // 10
        curr_num = curr_num % 10
        ans += curr_num*place
        place *= 10
        integer2 = integer2.next
    
    ans += carry*place
    return ans

if __name__ == "__main__":
    head1 = generate_linked_list_from_iterable([], True)
    head2 = generate_linked_list_from_iterable([1,2,3], True)
    ans = add_integers(head1,head2)
    print(ans)
    print()
    head1 = generate_linked_list_from_iterable([1,2,3], True)
    head2 = generate_linked_list_from_iterable([1,2,3], True)
    ans = add_integers(head1,head2)
    print(ans)
    print()
    head1 = generate_linked_list_from_iterable([1,0,9,9], True)
    head2 = generate_linked_list_from_iterable([7,3,2], True)
    ans = add_integers(head1,head2)
    print(ans)
    print()