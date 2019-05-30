from test_framework import generic_test
from test_framework.test_failure import TestFailure


def encoding(s):
    # TODO - you fill in here.
    p = 0
    i = 1
    count = 1
    res = []
    while p < len(s) and i < len(s):
        if s[i] == s[p]:
            count += 1
            i += 1
        else:
            res.extend([str(count), s[p]])
            p = i
            i = p + 1
            count = 1
    if p < len(s) and i >= len(s):
        res.extend([str(count), s[p]])
    return ''.join(res)


def decoding(s):
    # TODO - you fill in here.
    count, res = 0, []
    for i in range(len(s)):
        if s[i].isdigit():
            count = 10 * count + int(s[i])
        else:
            res.extend([s[i]] * count)
            count = 0
    return ''.join(res)

def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("run_length_compression.py",
                                       'run_length_compression.tsv',
                                       rle_tester))
