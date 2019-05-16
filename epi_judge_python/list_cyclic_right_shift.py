from test_framework import generic_test


def cyclically_right_shift_list(L, k):
		# TODO - you fill in here.
		def length(L):
			c = L
			cnt = 0
			while c:
				cnt += 1
				c = c.next
			return cnt
		
		if not L: return L
		k = k % length(L)
		if not k: return L
		c1 = c2 = L
		for _ in range(k):
			c2 = c2.next
		while c2.next:
			c2 = c2.next
			c1 = c1.next
		new_head = c1.next
		c1.next = None
		c2.next = L
		return new_head


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("list_cyclic_right_shift.py",
																			 'list_cyclic_right_shift.tsv',
																			 cyclically_right_shift_list))
