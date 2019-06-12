from test_framework import generic_test


def get_max_trapped_water(heights):
    i = 0
    j = len(heights) - 1

    max_trapped_water = float('-inf')
    while i <= j:
        if heights[i] < heights[j]:
            val = (j - i) * heights[i]
            i += 1
        elif heights[i] == heights[j]:
            val = (j - i) * heights[i]
            i, j = i + 1, j - 1
        else:
            val = (j - i) * heights[j]
            j -= 1

        max_trapped_water = max(val, max_trapped_water)
    return max_trapped_water


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.py",
                                       "max_trapped_water.tsv",
                                       get_max_trapped_water))
