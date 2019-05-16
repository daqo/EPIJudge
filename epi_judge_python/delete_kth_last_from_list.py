from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    # TODO - you fill in here.
    c1 = c2 = L
    for _ in range(k):
    	c2 = c2.next
    if not c2:
    	return L.next
    while c2.next:
    	c1 = c1.next
    	c2 = c2.next
    c1.next = c1.next.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
