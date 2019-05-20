from test_framework import generic_test


def inorder_traversal(tree):
    # TODO - you fill in here.
    result, s = [], []
    while s or tree:
    	if tree:
    		s.append(tree)
    		tree = tree.left
    	else:
    		item = s.pop()
    		result.append(item.data)
    		tree = item.right
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
