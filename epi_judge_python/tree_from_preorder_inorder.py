from test_framework import generic_test

from binary_tree_with_parent_prototype import BinaryTreeNode
def binary_tree_from_preorder_inorder(preorder, inorder):
		node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}
		def construct(preorder_start, preorder_finish, inorder_start, inorder_finish):
			if preorder_start >= preorder_finish or inorder_start >= inorder_finish: return
			root_data = preorder[preorder_start]
			idx = node_to_inorder_idx[root_data]
			# idx = inorder.index(root_data)
			left_subtree_size = idx - inorder_start
			root = BinaryTreeNode(root_data)
			root.left = construct(preorder_start + 1, preorder_start + 1 + left_subtree_size, inorder_start, idx)
			root.right = construct(preorder_start + 1 + left_subtree_size, preorder_finish, idx + 1, inorder_finish)
			return root
		return construct(0, len(preorder), 0, len(inorder))


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("tree_from_preorder_inorder.py",
																			 'tree_from_preorder_inorder.tsv',
																			 binary_tree_from_preorder_inorder))
