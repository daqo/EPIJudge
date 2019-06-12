from test_framework import generic_test


def number_of_ways_to_top(top, maximum_step):
    def helper(h):
        if h <= 1:
            return 1
        if number_of_ways_to_h[h] == 0:
            cnt = 0
            for i in range(1, min(h, maximum_step) + 1):
                cnt += helper(h - i)
            number_of_ways_to_h[h] = cnt
        return number_of_ways_to_h[h]

    number_of_ways_to_h = [0] * (top + 1)
    return helper(top)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_staircase.py",
                                       "number_of_traversals_staircase.tsv",
                                       number_of_ways_to_top))
