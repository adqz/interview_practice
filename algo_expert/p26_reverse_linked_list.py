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
    
    return next_node