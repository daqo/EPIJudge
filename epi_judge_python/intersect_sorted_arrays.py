from test_framework import generic_test

def intersect_two_sorted_arrays(A, B):
		# TODO - you fill in here.
		result = []
		i = 0
		j = 0
		while i < len(A) and j < len(B):
			if A[i] == B[j]:
				if (not result) or (result and result[-1] != A[i]):
					result.append(A[i])
				i, j = i + 1, j + 1
			elif A[i] < B[j]:
				i += 1
			else:
				j += 1
		return result

if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("intersect_sorted_arrays.py",
																			 'intersect_sorted_arrays.tsv',
																			 intersect_two_sorted_arrays))
