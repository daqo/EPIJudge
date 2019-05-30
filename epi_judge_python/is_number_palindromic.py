from test_framework import generic_test


def is_palindrome_number(x):
    def reverse(x):
    	res = 0
    	x_copy = abs(x)
    	while x_copy:
    		res = 10 * res + x_copy % 10
    		x_copy //= 10
    	return -res if x < 0 else res

    if x <= 0:
    	return x == 0
    return reverse(x) == x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
