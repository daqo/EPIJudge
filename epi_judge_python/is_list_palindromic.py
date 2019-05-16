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

def is_linked_list_a_palindrome(L):
		# TODO - you fill in here.
		def length(L):
			cnt = 0
			while L:
				cnt += 1
				L = L.next
			return cnt

		slow = fast = L
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		L = reverse_sublist(L, length(L) // 2 + 1,length(L))

		fast = slow = L
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		c = L
		orig_slow = slow
		while c and c is not orig_slow:
			if c.data != slow.data: 
				return False
			c = c.next
			slow = slow.next
		return True


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("is_list_palindromic.py",
																			 'is_list_palindromic.tsv',
																			 is_linked_list_a_palindrome))
