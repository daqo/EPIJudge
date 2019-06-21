from test_framework import generic_test

WHITE, BLACK = range(2)
import collections
def fill_surrounded_regions(board):
    n, m = len(board), len(board[0])
    q = collections.deque()
    for j in range(0, m):
        if board[0][j] == 'W':
            q.append((0, j))
    
    for i in range(0, n):
        if board[i][0] == 'W':
            q.append((i, 0))

    for j in range(0, m):
        if board[n - 1][j] == 'W':
            q.append((n - 1, j))
    
    for i in range(0, n):
        if board[i][m - 1] == 'W':
            q.append((i, m - 1))

    while q:
        x, y = q.popleft()
        if (0 <= x < n and 0 <= y < m) and board[x][y] == 'W':
            board[x][y] = 'T'
            q.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'T':
                board[i][j] = 'W'
            else: 
                board[i][j] = 'B'

def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
