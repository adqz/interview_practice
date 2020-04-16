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

# O(n) time | O(1) space
def delete_node(head, key):
    # 1. If key is head, keep shifting head to next node
    while head and head.data == key:
        head = head.next
    # 2. If head is None, return None
    if not head:
        return None
    # 3. Start from the node after head and remove if node.data == key
    prev_node = head
    node = head.next
    while node and node.next:
        if node.data == key:
            prev_node.next = node.next
        else:
            prev_node = node
        
        node = node.next
    
    if node.data == key:
        prev_node.next = None

    return head


if __name__ == "__main__":
    head = generate_linked_list_from_iterable([1,4,2], True)
    ans = delete_node(head, 4)
    print_linked_list(ans)
    print()
    head = generate_linked_list_from_iterable([4,1,4,2], True)
    ans = delete_node(head, 4)
    print_linked_list(ans)
    print()
    head = generate_linked_list_from_iterable([4,4,4,4], True)
    ans = delete_node(head, 4)
    print_linked_list(ans)
    print()
    head = generate_linked_list_from_iterable([4, 6, 20, 1], True)
    ans = delete_node(head, 1)
    print_linked_list(ans)
    print()
    head = generate_linked_list_from_iterable([4, 6, 20, 1], True)
    ans = delete_node(head, 4)
    print_linked_list(ans)