from test_framework import generic_test, test_utils

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')
def phone_mnemonic(phone_number):
		# TODO - you fill in here.

		## iterative version
		# def helper(results, digit):
		# 	partial_results = []
		# 	for item in results:
		# 		for mapping in MAPPING[int(digit)]:
		# 			partial_results.append(item + mapping)
		# 	return partial_results

		# results = []
		# for digit in phone_number:
		# 	if not results:
		# 		for mapping in MAPPING[int(digit)]:
		# 			results.append(mapping)
		# 	else:
		# 		results = helper(results, digit)
		# return results

		## recursive version
		def recursive_helper(res, number):
			if not number: return res
			partial_results = []
			for item in res:
				for mapping in MAPPING[int(number[0])]:
					partial_results.append(item + mapping)
			return recursive_helper(partial_results, number[1:])

		res = []
		for mapping in MAPPING[int(phone_number[0])]:
			res.append(mapping)
		return recursive_helper(res, phone_number[1:])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))