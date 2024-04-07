def loop_size(node):
    obj_1 = node.next
    obj_2 = node.next.next
    while obj_1 != obj_2:
        obj_1 = obj_1.next
        obj_2 = obj_2.next.next
    obj_1 = node
    while obj_1 != obj_2:
        obj_1 = obj_1.next
        obj_2 = obj_2.next
    loop_length = 1
    current = obj_1.next
    while current != obj_1:
        loop_length += 1
        current = current.next
    return loop_length