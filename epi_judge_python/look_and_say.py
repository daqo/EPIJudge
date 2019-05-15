from test_framework import generic_test


def look_and_say(n):
    # TODO - you fill in here.
		if n == 1: return '1'
		s = look_and_say(n - 1)
		p = s[0]
		count = 0
		final = []
		for i in range(len(s)):
			if s[i] == p:
				count += 1
			else:
				final.append(str(count))
				final.append(str(p))
				count = 1
				p = s[i]
		final.append(str(count))
		final.append(str(p))
		return ''.join(final)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))