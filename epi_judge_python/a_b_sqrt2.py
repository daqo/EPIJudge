from test_framework import generic_test

from math import sqrt
import bintrees
import heapq
def generate_first_k_a_b_sqrt2(k):
		def calc(a, b): return a + b * sqrt(2)
		###### using a BST
		candidates = bintrees.RBTree([(0, (0, 0))])
		res = []
		while len(res) < k:
			a, b = candidates.pop_min()[1]
			res.append(calc(a, b))
			candidates.insert(calc(a + 1, b), (a + 1, b))
			candidates.insert(calc(a, b + 1), (a, b + 1))
		return res

		###### using a minheap
		# candidates = [(0, (0, 0))]
		# res = []
		# while len(res) < k:
		# 	min_val, (a, b) = heapq.heappop(candidates)
		# 	if min_val not in res:
		# 		res.append(min_val)
		# 		heapq.heappush(candidates, (calc(a + 1, b), (a + 1, b)))
		# 		heapq.heappush(candidates, (calc(a, b + 1), (a, b + 1)))
		# return res

if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("a_b_sqrt2.py", 'a_b_sqrt2.tsv',
																			 generate_first_k_a_b_sqrt2))
