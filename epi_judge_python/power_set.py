from test_framework import generic_test, test_utils


def generate_power_set(S):
		if len(S) == 0:
			return [[]]
		elif len(S) == 1:
			return [[], [S[0]]]
		res = []
		items = generate_power_set(S[1:])
		res.extend(items.copy())
		for item in items:
			item_copy = item.copy()
			item_copy.append(S[0])
			res.append(item_copy)
		return res

if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("power_set.py", 'power_set.tsv',
																			 generate_power_set,
																			 test_utils.unordered_compare))
