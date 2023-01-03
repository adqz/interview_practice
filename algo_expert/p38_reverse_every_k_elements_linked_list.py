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

def reverse_k_nodes(head, k):
    if not head: return head
    if k <= 1: return head

    slow = head
    fast = slow
    counter = 1
    while fast.next and counter < k:
        fast = fast.next
        counter += 1
    
    head1 = slow
    head2 = fast.next
    fast.next = None
    
    while head1.next is not None:
        head1 = head1.next
    
    head1.next = reverse_k_nodes(head2, k)

    return head

def reverse(head):
    node = head
    if node.next == None:
        return head
    
    prev_node = None
    # 1. Reverse links until last element
    while node.next != None and node.next.next != None:
        next_node = node.next
        next_next_node = node.next.next

        # Reverse
        next_node.next = node
        node.next = prev_node
        node = next_next_node
        prev_node = next_node
    
    # 2. Reverse last link
    if node.next != None:
        next_node = node.next
        node.next = prev_node
        next_node.next = node
    else:
        node.next = prev_node
        next_node = node

    return next_node

if __name__ == "__main__":
    head = generate_linked_list_from_iterable([1,2,3,4,5], True)
    ans = reverse_k_nodes(head, 3)
    # print_linked_list(ans)
    # print()