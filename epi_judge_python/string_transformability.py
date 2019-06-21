from test_framework import generic_test


# Uses BFS to find the least steps of transformation.
import collections
import string
def transform_string(D, s, t):
    q = collections.deque([(s, 0)])
    visited = collections.defaultdict(bool)
    while q:
        vertex, cnt = q.popleft()
        if vertex == t:
            return cnt
        visited[vertex] = True
        for i in range(len(vertex)):
            for c in string.ascii_lowercase:
                cand = vertex[:i] + c + vertex[i + 1:]
                if cand in D and not visited[cand]:
                    q.append((cand, cnt + 1))
    return -1




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
