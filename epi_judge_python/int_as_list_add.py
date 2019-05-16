from list_node import ListNode
from test_framework import generic_test

def add_two_numbers(L1, L2):
    # TODO - you fill in here.
    prev = prehead = ListNode()
    carry = 0
    while L1 or L2 or carry:
    	new_node = ListNode()
    	prev.next = new_node
    	prev = prev.next
    	val = (L1.data if L1 else 0) + (L2.data if L2 else 0) + carry
    	if val < 10:
    		new_node.data = val
    		carry = 0
    	else:
    		new_node.data = val - 10
    		carry = 1
    	L1 = L1.next if L1 else None
    	L2 = L2.next if L2 else None
    return prehead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
