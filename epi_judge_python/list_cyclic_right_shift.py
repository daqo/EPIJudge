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
		c = L
		p = None
		for _ in range(length(L) - k):
			p = c
			c = c.next
		new_head = c
		p.next = None
		while c.next:
			c = c.next
		c.next = L
		return new_head


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("list_cyclic_right_shift.py",
																			 'list_cyclic_right_shift.tsv',
																			 cyclically_right_shift_list))
