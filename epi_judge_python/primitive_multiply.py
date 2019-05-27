from test_framework import generic_test


def multiply(x, y):
		def add(x, y):
			running_sum = 0
			carryin = 0
			temp_x = x
			temp_y = y
			k = 1
			while temp_x or temp_y:
					ak = x & k
					bk = y & k
					carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
					running_sum |= ak ^ bk ^ carryin
					carryin = carryout << 1
					k = k << 1
					temp_x = temp_x >> 1
					temp_y = temp_y >> 1
			return running_sum | carryin

		running_sum = 0
		while x:
			if x & 1:
				running_sum = add(running_sum, y)
			x >>= 1
			y <<= 1
		return running_sum


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("primitive_multiply.py",
																			 'primitive_multiply.tsv', multiply))
