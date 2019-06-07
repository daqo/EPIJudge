from test_framework import generic_test


def matrix_search(A, x):
    n = len(A)
    m = len(A[0])
    i, j = 0, m - 1
    while 0 <= i < n and 0 <= j < m:
    	if x == A[i][j]:
    		return True
    	elif x < A[i][j]:
    		j -= 1
    	else:
    		i += 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
