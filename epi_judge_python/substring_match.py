from test_framework import generic_test


def rabin_karp(t, s):
		if len(s) > len(t): return -1
		# bruteforce solution
		# for i in range(len(t) - len(s) + 1):
		# 	if t[i:i + len(s)] == s:
		# 		return i
		# return -1
		def rolling_hash(result, c): return ord(c) + result * 31
		def extract_hash(result, c):
			cnt = len(s) - 1
			return result - (31 ** cnt) * ord(c)

		hs = 0
		for i in range(len(s)):
			hs = rolling_hash(hs, s[i])
		ht = 0
		for i in range(len(s)):
			ht = rolling_hash(ht, t[i])
		if hs == ht:
			if t[0:len(s)] == s:
				return 0

		for i in range(len(s), len(t)):
			ht = extract_hash(ht, t[i - len(s)])
			ht = rolling_hash(ht, t[i])
			if hs == ht:
				if t[i - len(s) + 1: i + 1] == s:
					return i - len(s) + 1
		return -1

if __name__ == '__main__':
		exit(
				generic_test.generic_test_main("substring_match.py",
																			 'substring_match.tsv', rabin_karp))
