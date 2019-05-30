from test_framework import generic_test


def plus_one(A):
    # TODO - you fill in here.
    A[-1] += 1
    carry = 0
    for i in reversed(range(len(A))):
    	val = A[i] + carry 
    	if val > 9:
    		A[i] = val % 10
    		carry = 1
    	else:
    		A[i] = val
    		carry = 0
    if carry:
    	A.insert(0, carry)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
