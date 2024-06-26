class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if not source:
        raise ValueError("Source list is empty")
    move = source
    source = source.next
    if dest:
        move.next = dest
    dest = move
    return Context(source, dest)