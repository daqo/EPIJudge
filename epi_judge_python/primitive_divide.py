from test_framework import generic_test


def divide(x, origy):
		k, result = 0, 0
		while x >= origy:
			y = origy
			k = 0
			while x >= y:
				prev = y
				y <<= 1
				k += 1
			result += (1 << (k - 1))
			x = x - prev
		return result


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("primitive_divide.py",
																			 "primitive_divide.tsv", divide))
