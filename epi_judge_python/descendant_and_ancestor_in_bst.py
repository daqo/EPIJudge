import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(node0, node1, middle):
    # TODO - you fill in here.
    def search(tree, node):
        c = tree
        while c: 
            if c.data == node.data:
                return node
            elif c.data < node.data:
                c = c.right
            else:
                c = c.left
        return None
    found_ancestor = found_descendant = False
    if search(node0, middle) and node0.data != middle.data:
        found_ancestor = True
        if search(middle, node1) and node1.data != middle.data:
            found_descendant = True
    if found_ancestor and found_descendant: return True
    if found_ancestor and not found_descendant: return False

    if search(node1, middle) and node1.data != middle.data:
        found_ancestor = True
        if search(middle, node0) and node0.data != middle.data:
            found_descendant = True
    return found_ancestor and found_descendant


@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(
        executor, tree, node0, node1,
        middle_idx):
    candidate0 = must_find_node(tree, node0)
    candidate1 = must_find_node(tree, node1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "descendant_and_ancestor_in_bst.py",
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))
