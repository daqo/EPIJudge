from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs):
		def backtrack(S = '', left = 0, right = 0):
				if len(S) == 2 * num_pairs:
						ans.append(S)
						return
				if left < num_pairs:
						backtrack(S + '(', left + 1, right)
				if right < left:
						backtrack(S + ')', left, right + 1)
		ans = []
		backtrack()
		return ans


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("enumerate_balanced_parentheses.py",
																			 'enumerate_balanced_parentheses.tsv',
																			 generate_balanced_parentheses,
																			 test_utils.unordered_compare))
