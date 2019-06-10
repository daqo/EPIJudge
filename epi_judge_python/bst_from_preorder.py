from test_framework import generic_test

from bst_node import BstNode
def rebuild_bst_from_preorder(A):
		def rebuild_bst_from_preorder_on_value_range(lower_bound, higher_bound):
			global root_idx
			if root_idx == len(A): return
			root_val = A[root_idx]
			if not lower_bound <= root_val <= higher_bound:
				return
			root = BstNode(root_val)
			root_idx += 1
			root.left = rebuild_bst_from_preorder_on_value_range(lower_bound, root_val)
			root.right = rebuild_bst_from_preorder_on_value_range(root_val, higher_bound)
			return root

		global root_idx
		root_idx = 0
		return rebuild_bst_from_preorder_on_value_range(float('-inf'), float('inf'))
if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("bst_from_preorder.py",
																			 'bst_from_preorder.tsv',
																			 rebuild_bst_from_preorder))
