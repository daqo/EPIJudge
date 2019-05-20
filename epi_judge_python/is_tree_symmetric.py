from test_framework import generic_test


def is_symmetric(tree):
		def check(l_tree, r_tree):
			if not l_tree and not r_tree: return True
			if l_tree and not r_tree: return False
			if not l_tree and r_tree: return False
			if l_tree.data == r_tree.data:
				if not check(l_tree.left, r_tree.right):
					return False
				if not check(l_tree.right, r_tree.left):
					return False
			else: return False
			return True
		if not tree: return True
		return check(tree.left, tree.right)


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("is_tree_symmetric.py",
																			 'is_tree_symmetric.tsv', is_symmetric))
