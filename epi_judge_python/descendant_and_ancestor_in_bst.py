import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(node0, node1, middle):
	def search(start, target):
		c = start
		while c:
			if target.data < c.data:
				c = c.left
			elif target.data > c.data:
				c = c.right
			else:
				return target is not start
		return False

	return (search(middle, node0) and search(node1, middle)) or \
		   (search(middle, node1) and search(node0, middle))

@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(
		executor, tree, node0, node1,
		middle_idx):
	candidate0 = must_find_node(tree, node0)
	candidate1 = must_find_node(tree, node1)
	middle_node = must_find_node(tree, middle_idx)

	return executor.run(
		functools.partial(pair_includes_ancestor_and_descendant_of_m,
						  candidate0, candidate1, middle_node))


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"descendant_and_ancestor_in_bst.py",
			'descendant_and_ancestor_in_bst.tsv',
			pair_includes_ancestor_and_descendant_of_m_wrapper))
