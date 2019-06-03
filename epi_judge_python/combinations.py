from test_framework import generic_test, test_utils

def combinations(n, k):
		# TODO - you fill in here.
		def helper(A, k):
			if len(A) < k or k == 0:
				return [[]]
			elif k == 1:
				return [[i] for i in A]
			res = []
			for item in helper(A[1:], k - 1):
				item_copy = item.copy()
				item_copy.append(A[0])
				res.append(item_copy)
			res.extend([item for item in helper(A[1:], k) if item])
			return res
		return helper(list(range(1, n + 1)), k)

if __name__ == '__main__':
		exit(
				generic_test.generic_test_main(
						"combinations.py",
						'combinations.tsv',
						combinations,
						comparator=test_utils.unordered_compare))
