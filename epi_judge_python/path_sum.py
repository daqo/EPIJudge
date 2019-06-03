from test_framework import generic_test


def has_path_sum(tree, remaining_weight):
    # TODO - you fill in here.
    if not tree: return False
    if not tree.left and not tree.right:
    	if tree.data == remaining_weight: return True
    if not has_path_sum(tree.left, remaining_weight - tree.data):
        return has_path_sum(tree.right, remaining_weight - tree.data)
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("path_sum.py", 'path_sum.tsv',
                                       has_path_sum))
