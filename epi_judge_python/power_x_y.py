from test_framework import generic_test


def power(x, y):
		res = 1.0
		if y < 0:
			x = 1.0 / x
			y = -y
		while y:
			if y & 1:
				res = res * x
			x = x * x
			y = y >> 1
		return res


if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
