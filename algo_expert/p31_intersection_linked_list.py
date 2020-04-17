# O(m+n) time | O(min(m,n)) space
def intersect(head1, head2):
    seen = set()
    # Adding all nodes of head2 in the "Seen" set
    while head2:
        seen.add(head2)
        head2 = head2.next
    # Iterating over all nodes in 1st list
    while head1:
        # If a node in the first list was already seen in the second list, then this is the first point of intersection!
        if head1 in seen:
            return head1
        head1 = head1.next
    
    return None