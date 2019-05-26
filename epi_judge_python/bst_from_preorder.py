from test_framework import generic_test

from bst_node import BstNode
def rebuild_bst_from_preorder(preorder_sequence):
		def helper(lower_bound, higher_bound):
			if root_idx[0] == len(preorder_sequence):
				return
			root_val = preorder_sequence[root_idx[0]]
			if not lower_bound <= root_val <= higher_bound:
				return
			root = BstNode(root_val)
			root_idx[0] += 1
			root.left = helper(lower_bound, root_val)
			root.right = helper(root_val, higher_bound)
			return root

		root_idx = [0]
		return helper(float('-inf'), float('inf'))
if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("bst_from_preorder.py",
																			 'bst_from_preorder.tsv',
																			 rebuild_bst_from_preorder))
