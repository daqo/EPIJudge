import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    # TODO - you fill in here.
    c0, c1 = node0, node1
    nodes_on_path_to_root = set()
    while c0 or c1:
        if c0:
            if c0 in nodes_on_path_to_root:
                return c0
            nodes_on_path_to_root.add(c0)
            c0 = c0.parent
        if c1:
            if c1 in nodes_on_path_to_root:
                return c1
            nodes_on_path_to_root.add(c1)
            c1 = c1.parent
    return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "lowest_common_ancestor_close_ancestor.py",
            'lowest_common_ancestor.tsv', lca_wrapper))
