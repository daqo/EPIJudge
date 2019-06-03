from test_framework import generic_test


def examine_buildings_with_sunset(sequence):
		# TODO - you fill in here.

		# solution without stack
		# results = []
		# max_so_far = float('-inf')
		# for i in reversed(range(len(sequence))):
		# 	if sequence[i] > max_so_far:
		# 		results.append(i)
		# 		max_so_far = sequence[i]
		# return results

		# solution with stack
		stack = []
		for building_idx, building_height in enumerate(sequence):
			while stack and building_height >= stack[-1][1]:
				stack.pop()
			stack.append((building_idx, building_height))
		return [c[0] for c in reversed(stack)]



def examine_buildings_with_sunset_wrapper(sequence):
		return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
																			 examine_buildings_with_sunset))
