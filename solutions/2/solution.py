class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(list_1, list_2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result_list = None
    last_node = None
    plus = 0
    while list_1 != None and list_2 != None:
        answer = list_1.val + list_2.val + plus

        if answer >= 10:
            answer = answer - 10
            plus = 1
        else:
            plus = 0

        if last_node is None:
            result_list = ListNode(answer)
            last_node = result_list
        else:
            last_node.next = ListNode(answer)
            last_node = last_node.next

        # move to next
        list_1 = list_1.next
        list_2 = list_2.next

    # move to end
    if list_1 is None:
        last_node.next = list_2
    if list_2 is None:
        last_node.next = list_1

    while plus > 0 and last_node.next != None:
        last_node = last_node.next
        last_node.val = last_node.val+plus
        if last_node.val >= 10:
            last_node.val = last_node.val - 10
            plus = 1
        else:
            plus = 0

    if plus > 0:
        last_node.next = ListNode(plus)
    return result_list


if __name__ == '__main__':
    L1 = ListNode(2)
    L1.next = ListNode(4)
    L1.next.next = ListNode(3)

    L2 = ListNode(5)
    L2.next = ListNode(6)
    L2.next.next = ListNode(4)
    print(add_two_numbers(L1, L2))
