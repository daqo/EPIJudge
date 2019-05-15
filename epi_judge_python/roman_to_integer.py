from test_framework import generic_test


def roman_to_integer(s):
    # TODO - you fill in here.
    T = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    res = 0
    p = 0
    i = 1
    while p < len(s) and i < len(s):
    	if (s[p] == 'I' and s[i] in ('V', 'X') or 
    		  s[p] == 'X' and s[i] in ('L', 'C') or 
    		  s[p] == 'C' and s[i] in ('D', 'M')):
    		res += T[s[i]]
    		res -= T[s[p]]
    		p = i + 1
    		i += 2
    	else:
    		res += T[s[p]]
    		p += 1
    		i += 1
    if i >= len(s) and p < len(s):
    	res += T[s[p]]
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
