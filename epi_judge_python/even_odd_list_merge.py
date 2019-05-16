from test_framework import generic_test

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def even_odd_merge(L):
    if not L: return L
    peven = even_prehead = ListNode('dummy-even')
    podd = odd_prehead = ListNode('dummy-odd')

    c = L
    cnt = -1
    while c:
    	cnt += 1
    	if cnt % 2 == 0:
    		peven.next = c
    		t = c.next
    		c.next = None
    		c = t
    		peven = peven.next
    	else:
    		podd.next = c
    		t = c.next
    		c.next = None
    		c = t
    		podd = podd.next
    peven.next = odd_prehead.next
    return even_prehead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
