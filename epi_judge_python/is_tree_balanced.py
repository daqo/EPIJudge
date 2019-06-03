from test_framework import generic_test


def is_balanced_binary_tree(tree):
		def is_balanced(tree):
			if not tree: return (True, 0)
			is_left_balanced, left_height = is_balanced(tree.left)
			is_right_balanced, right_height = is_balanced(tree.right)
			if not is_left_balanced or not is_right_balanced:
				return (False, -1)
			return (abs(left_height - right_height) <= 1, max(left_height, right_height) + 1)

		return is_balanced(tree)[0]




if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("is_tree_balanced.py",
																			 'is_tree_balanced.tsv',
																			 is_balanced_binary_tree))
