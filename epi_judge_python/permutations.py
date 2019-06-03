from test_framework import generic_test, test_utils

def permutations(A):
	if len(A) == 1:
		return [[A[0]]]
	res = []
	for item in permutations(A[1:]):
		t = []
		for i in range(len(item) + 1):
			item_copy = item.copy()
			item_copy.insert(i, A[0])
			t.append(item_copy)
		res.extend(t)
	return res

if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("permutations.py", 'permutations.tsv',
																			 permutations,
																			 test_utils.unordered_compare))
