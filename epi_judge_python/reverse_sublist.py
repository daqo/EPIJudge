from test_framework import generic_test

class ListNode:
	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

def reverse_sublist(L, start, finish):
    # TODO - you fill in here.
    if not L: return
    if not L.next: return L
    p = prehead = ListNode('dummy')
    p1 = ListNode('dummy1')
    prehead.next = L

    prev = None
    after = None
    c = prehead
    count = 0
    while c:
    	if count == start - 1:
    		prev = c
    	if count == finish + 1:
    		after = c
    	count += 1
    	c = c.next
    
    last_node = c = prev.next
    while c and c != after:
    	t = c.next
    	c.next = p1.next
    	p1.next = c
    	c = t
    prev.next = p1.next
    last_node.next = after
    return prehead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
