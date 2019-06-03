from test_framework import generic_test


def binary_tree_depth_order(tree):
		# TODO - you fill in here.
		if not tree: return []
		result = []
		q = [[tree]]
		while q:
			items = q.pop(0)
			result.append([item.data for item in items])
			tmp = [child for item in items for child in (item.left, item.right) if child]
			if tmp: q.append(tmp)
		return result





if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("tree_level_order.py",
																			 "tree_level_order.tsv",
																			 binary_tree_depth_order))
