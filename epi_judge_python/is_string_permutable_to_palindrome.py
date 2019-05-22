from test_framework import generic_test

import collections
def can_form_palindrome(s):
		# TODO - you fill in here.
		h = collections.defaultdict(int)
		for c in s:
			h[c] += 1
			h[c] = h[c] % 2
		return sum(h.values()) == 0 or sum(h.values()) == 1


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main(
						"is_string_permutable_to_palindrome.py",
						'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
