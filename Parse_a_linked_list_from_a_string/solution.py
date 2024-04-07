def linked_list_from_string(s):
    if s in ["null", "NULL", "nil", "nullptr", "null()"]:
        return None

    nodes = s.split(" -> ")
    if nodes[0] == "None":
        return None

    head = Node(int(nodes[0]))
    current = head
    for i in range(1, len(nodes)):
        if nodes[i] == "None":
            current.next = None
        else:
            current.next = Node(int(nodes[i]))
            current = current.next

    return head
    