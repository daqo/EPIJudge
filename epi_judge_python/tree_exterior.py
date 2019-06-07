import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree):
    def list_of_leaves(tree):
        if not tree: return []
        if not tree.left and not tree.right: return [tree]
        return list_of_leaves(tree.left) + list_of_leaves(tree.right)
    left = []
    c = tree
    while c:
        left.append(c)
        prev = c
        c = c.left
        if c is None:
            c = prev.right
    left and left.pop()

    bottom = list_of_leaves(tree)

    right = []
    c = tree
    while c:
        right.append(c)
        prev = c
        c = c.right
        if c is None:
            c = prev.left
    right and right.pop(0)
    right and right.pop()
    return left + bottom + list(reversed(right))


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_exterior.py", 'tree_exterior.tsv',
                                       create_output_list_wrapper))
