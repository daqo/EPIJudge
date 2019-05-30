from test_framework import generic_test


def can_reach_end(A):
		furthest_reach_so_far = 0
		i = 0
		while i <= furthest_reach_so_far and i < len(A):
			furthest_reach_so_far = max(furthest_reach_so_far, i + A[i])
			i += 1
		return furthest_reach_so_far >= len(A) - 1


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main(
						"advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
