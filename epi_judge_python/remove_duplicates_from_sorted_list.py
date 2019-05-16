from test_framework import generic_test


def remove_duplicates(L):
    # TODO - you fill in here.
    if not L: return L
    p = L
    c = L.next
    while c:
    	if c.data == p.data:
    		p.next = c.next
    		c = c.next
    	else:
    		p = c
    		c = c.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
