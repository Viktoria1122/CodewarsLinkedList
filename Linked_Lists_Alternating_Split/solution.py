class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError("List should have two nodes for splitting")
    first_obj = Node()
    second_obj = Node()
    first_cur = first_obj
    second_cur = second_obj
    cur = head
    count = 1
    while cur:
        if count % 2 != 0:
            first_cur.next = cur
            first_cur = first_cur.next
        else:
            second_cur.next = cur
            second_cur = second_cur.next
        cur = cur.next
        count += 1
    first_cur.next = None
    second_cur.next = None
    return Context(first_obj.next, second_obj.next)