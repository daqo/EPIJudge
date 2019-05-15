from test_framework import generic_test

def rotate_matrix(square_matrix):
    # TODO - you fill in here.
    def rotate(A, M, row_idx, col_idx):
    	for j in range(0, n):
    		A[j][col_idx] = M[row_idx][j]

    n = len(square_matrix)
    A = [[float('inf') for x in range(n)] for y in range(n)]
    for i in range(n):
	    rotate(A, square_matrix, i, n - i - 1)
    for i in range(n):
    	for j in range(n):
    		square_matrix[i][j] = A[i][j]

def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_rotation.py",
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
