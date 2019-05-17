from test_framework import generic_test


def binary_tree_depth_order(tree):
		# TODO - you fill in here.
		if not tree: return []
		result = []
		queue = [tree]
		while queue:
			# temp = []
			# for item in queue:
			# 	temp.append(item.data)
			# result.append(temp)
			result.append([item.data for item in queue])

			# temp = []	
			# for curr in queue:
			# 	if curr.left: temp.append(curr.left)
			# 	if curr.right:temp.append(curr.right)
			# queue = temp
			queue = [child for curr in queue for child in (curr.left, curr.right) if child]
		return result





if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("tree_level_order.py",
																			 "tree_level_order.tsv",
																			 binary_tree_depth_order))
