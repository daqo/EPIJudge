from test_framework import generic_test


import math
# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(A):
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n = len(A)
    # Check row and column constraints.
    for i in range(n):
        if has_duplicate(A[i]):
            return False
    for item in [[A[i][j] for i in range(n)] for j in range(n)]:
        if has_duplicate(item):
            return False
    # if any(
    #         has_duplicate([A[i][j] for j in range(n)])
    #         or has_duplicate([A[j][i] for j in range(n)])
    #         for i in range(n)):
    #     return False

    # Check region constraints.
    region_size = int(math.sqrt(n))
    # return all(not has_duplicate([
    #     A[a][b]
    #     for a in range(region_size * I, region_size * (
    #         I + 1)) for b in range(region_size * J, region_size * (J + 1))
    # ]) for I in range(region_size) for J in range(region_size))
    regions = []
    for x in range(0, n, region_size):
        for y in range(0, n, region_size):
            l = []
            for i in range(x, x + region_size):
                for j in range(y, y + region_size):
                    l.append(A[i][j])
            regions.append(l)
    for item in regions:
        if has_duplicate(item):
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
