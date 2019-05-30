from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
  def spiral_order(M, p, r):
    if p >= r: return []
    res = []
    res.extend(M[p][j] for j in range(p, r))
    res.extend(M[i][r - 1] for i in range(p + 1, r))
    res.extend(M[r - 1][j] for j in reversed(range(p, r - 1)))
    res.extend(M[i][p] for i in reversed(range(p + 1, r - 1)))
    res.extend(spiral_order(M, p + 1, r - 1))
    return res


  return spiral_order(square_matrix, 0, len(square_matrix))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
