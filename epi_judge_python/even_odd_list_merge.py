from test_framework import generic_test

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def even_odd_merge(L):
	if not L: return L
	evens = L
	odds = L.next
	c0 = evens
	c1 = odds
	while c0 and c1:
		last = c0
		c0.next = c0.next and c0.next.next
		c0 = c0.next
		c1.next = c1.next and c1.next.next
		c1 = c1.next
	if c0:
		c0.next = odds
	else:
		last.next = odds
	return evens


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
