import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    # TODO - you fill in here.
    def reverse_range(s, start, finish):
    	while start < finish:
    		s[start], s[finish] = s[finish], s[start]
    		start += 1
    		finish -= 1
    start = 0
    s.reverse()
    while True:
        finish = s.find(b' ', start)
        if finish == -1:
            break
        reverse_range(s, start, finish - 1)
        start = finish + 1
    reverse_range(s, start, len(s) - 1)
    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
