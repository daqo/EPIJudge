from test_framework import generic_test
from list_node import ListNode

def stable_sort_list(L):
    # TODO - you fill in here.

    # insertion sort
    # if not L: return L
    # prev = prehead = ListNode('dummy')
    # c = L
    # while c:
    # 	prev = prehead
    # 	while prev.next and c.data > prev.next.data:
    # 		prev = prev.next
    # 	temp = c.next
    # 	c.next = prev.next
    # 	prev.next = c
    # 	c = temp
    # return prehead.next

    # mergesort
    def merge_two_sorted_lists(L1, L2):
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
    
    if not L or not L.next: return L
    slow, fast = L, L
    pre_slow = None
    while fast and fast.next:
    	pre_slow = slow
    	slow = slow.next
    	fast = fast.next.next
    pre_slow.next = None
    head1 = stable_sort_list(slow)
    head2 = stable_sort_list(L)
    return merge_two_sorted_lists(head1, head2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))
