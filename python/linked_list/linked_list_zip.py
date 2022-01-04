from linked_list.linked_list import LinkedList

def zip_lists_new(ll_one, ll_two):
    current_one = ll_one.head
    current_two = ll_two.head
    result = LinkedList()
    while current_one or current_two:
        if current_one:
            result.append(current_one.value)
            current_one = current_one.next
        if current_two:
            result.append(current_two.value)
            current_two = current_two.next
    return result
