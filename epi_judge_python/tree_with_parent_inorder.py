from test_framework import generic_test


def inorder_traversal(tree):
    result = []
    prev = None
    while tree:
    	if prev and prev is tree.right:
    		prev, tree = tree, tree.parent
    	else:
	    	while tree.left and tree.left is not prev:
	    		tree = tree.left
	    	result.append(tree.data)
	    	prev, tree = tree, tree.right if tree.right else tree.parent
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
