from test_framework import generic_test


def preorder_traversal(tree):
    # TODO - you fill in here.
    result, s = [], []
    while s or tree:
    	if tree:
    		result.append(tree.data)
    		s.append(tree)
    		tree = tree.left
    	else:
    		item = s.pop()
    		tree = item.right
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))
