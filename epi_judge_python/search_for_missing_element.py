import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
											 ('duplicate', 'missing'))


def find_duplicate_missing(A):
	xor1 = 0
	for i in range(len(A)):
		xor1 ^= i

	xor2 = 0
	for n in A:
		xor2 ^= n

	difference = xor1 ^ xor2
	lowest_set_bit = difference & ~(difference - 1)
	y1 = 0
	for i in range(len(A)):
		if i & lowest_set_bit:
			y1 ^= i
	y2 = 0
	for n in A:
		if n & lowest_set_bit:
			y2 ^= n
	miss_or_dup = y1 ^ y2
	if miss_or_dup in A:
		duplicate = miss_or_dup
		missing = duplicate ^ difference
	else:
		missing = miss_or_dup
		duplicate = missing ^ difference
	return DuplicateAndMissing(duplicate, missing)


def res_printer(prop, value):
	def fmt(x):
		return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

	if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
		return fmt(value)
	else:
		return value


if __name__ == '__main__':
	exit(
		generic_test.generic_test_main(
			"search_for_missing_element.py",
			'find_missing_and_duplicate.tsv',
			find_duplicate_missing,
			res_printer=res_printer))