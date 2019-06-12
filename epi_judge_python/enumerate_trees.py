import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from binary_tree_with_parent_prototype import BinaryTreeNode
def generate_all_binary_trees(num_nodes):
    # TODO - you fill in here.
    if num_nodes == 0:
        return [None]
    result = []
    for num_nodes_left_subtree in range(0, num_nodes):
        num_nodes_right_subtree = num_nodes - 1 - num_nodes_left_subtree
        left_subtrees = generate_all_binary_trees(num_nodes_left_subtree)
        right_subtrees = generate_all_binary_trees(num_nodes_right_subtree)
        for left in left_subtrees:
            for right in right_subtrees:
                result.append(BinaryTreeNode(0, left, right))
    return result

def serialize_structure(tree):
    result = []
    q = [tree]
    while q:
        a = q.pop(0)
        result.append(0 if not a else 1)
        if a:
            q.append(a.left)
            q.append(a.right)
    return result


@enable_executor_hook
def generate_all_binary_trees_wrapper(executor, num_nodes):
    result = executor.run(
        functools.partial(generate_all_binary_trees, num_nodes))

    return sorted(map(serialize_structure, result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_trees.py",
                                       'enumerate_trees.tsv',
                                       generate_all_binary_trees_wrapper))
