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
def remove_duplicates(head):

    if head == None:
        return head

    node = head
    seen = set()
    prev_node = None
    while node != None and node.next != None:
        # Remove link if duplicate
        if node.data in seen:
            prev_node.next = node.next
        else:
            seen.add(node.data)
            prev_node = node
        node = node.next
    
    if node != None and node.data in seen:
        prev_node.next = None

    return head

if __name__ == "__main__":
    head_1 = generate_linked_list_from_iterable([4,1,4,2], True)
    ans_1 = remove_duplicates(head_1)
    print_linked_list(ans_1)

    head_1 = generate_linked_list_from_iterable([4,4,4,4], True)
    ans_1 = remove_duplicates(head_1)
    print_linked_list(ans_1)

    head_1 = generate_linked_list_from_iterable([], True)
    ans_1 = remove_duplicates(head_1)
    print_linked_list(ans_1)

    head_1 = generate_linked_list_from_iterable([2,1,4,5,2,1,2,1,1], True)
    ans_1 = remove_duplicates(head_1)
    print_linked_list(ans_1)