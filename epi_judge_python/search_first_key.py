from test_framework import generic_test


def search_first_of_k(A, key):
    # TODO - you fill in here.
    p = 0
    r = len(A) - 1
    while p <= r:
        q = (p + r) // 2
        if A[q] == key:
            r = q
            if p == r: return r
        elif A[q] < key:
            p = q + 1
        else:
            r = q - 1
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))

# def search_last_of_k(A, k):
#     # TODO - you fill in here.
#     L = 0
#     U = len(A) - 1
#     result = -1
#     while L <= U:
#     	M = (L + U) // 2
#     	if A[M] == k:
#     		result = M
#     		L = M + 1
#     	elif A[M] < k:
#     		L = M + 1
#     	else: 
#     		U = M - 1
#     if result == -1:
#     	if U < 0: result = L
#     	else: result = U
#     else: result += 1
#     return result

# A = [-14,-10,2,108,108,243,285,285,285,401]
# search_last_of_k(A, -13)
# search_last_of_k(A, -8)
# search_last_of_k(A, 285)

# def search_first_last_of_k(A, k):
#     # TODO - you fill in here.
#     L = 0
#     U = len(A) - 1
#     pair = [-1, -1]
#     while L <= U:
#     	M = (L + U) // 2
#     	if A[M] == k:
#     		result = M
#     		L = M + 1
#     	elif A[M] < k:
#     		L = M + 1
#     	else: 
#     		U = M - 1
#     pair[1] = result
#     L = 0
#     U = pair[1]
#     while L <= U:
#     	M = (L + U) // 2
#     	if A[M] == k:
#     		result = M
#     		U = M - 1
#     	elif A[M] < k:
#     		L = M + 1
#     	else: 
#     		U = M - 1
#     pair[0] = result
#     return pair

# A = [1,2,2,4,4,4,7,11,11,13]
# search_first_last_of_k(A, 11)
