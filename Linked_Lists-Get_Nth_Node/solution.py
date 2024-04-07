from preloaded import Node

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    if not node or index < 0:
        raise ValueError("Invalid index")

    current = node
    count = 0
    while current:
        if count == index:
            return current
        count += 1
        current = current.next

    raise ValueError("Index out of range")