from test_framework import generic_test

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

def merge_two_sorted_lists(L1, L2):
    # TODO - you fill in here.
    prehead = ListNode('dummy')
    p = prehead
    while L1 and L2:
    	if L1.data < L2.data:
    		p.next = L1
    		p = p.next
    		L1 = L1.next
    	else:
    		p.next = L2
    		p = p.next
    		L2 = L2.next
    while L1:
    		p.next = L1
    		p = p.next
    		L1 = L1.next
    while L2:
    		p.next = L2
    		p = p.next
    		L2 = L2.next
    return prehead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
