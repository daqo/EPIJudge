import collections

from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree, interval):
		# TODO - you fill in here.
		def traverse(tree):
			if not tree: return
			if interval.left <= tree.data <= interval.right:
				traverse(tree.left)
				result.append(tree.data)
				traverse(tree.right)
			elif interval.left > tree.data:
				traverse(tree.right)
			else:
				traverse(tree.left)

		result = []
		traverse(tree)
		return result



def range_lookup_in_bst_wrapper(tree, i):
		return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("range_lookup_in_bst.py",
																			 'range_lookup_in_bst.tsv',
																			 range_lookup_in_bst_wrapper))
