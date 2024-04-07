from preloaded import Node

def swap_pairs(head):
    obj = Node()
    obj.next = head
    current = obj
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        first.next = second.next
        second.next = first
        current.next = second
        current = current.next.next

    return obj.next