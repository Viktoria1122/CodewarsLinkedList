""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    node = Node(data)
    if not head or head.data >= node.data:
        node.next = head
        return node
    current = head
    while current.next and current.next.data < node.data:
        current = current.next
    node.next = current.next
    current.next = node
    return head