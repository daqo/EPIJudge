from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
		# TODO - you fill in here.
		def helper(tree):
			if not tree: return
			if len(A) < k: helper(tree.right)
			if len(A) < k: A.append(tree.data)
			if len(A) < k: helper(tree.left)
		A = []
		helper(tree)
		return A

if __name__ == '__main__':
		exit(
				generic_test.generic_test_main(
						"k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
						find_k_largest_in_bst, test_utils.unordered_compare))
