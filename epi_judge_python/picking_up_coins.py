from test_framework import generic_test


def maximum_revenue(coins):
    def sum_coins(i, j):
        running_sum = 0
        for i in range(i, j + 1):
            running_sum += coins[i]
        return running_sum

    def helper(a, b):
        if a > b:
            return 0
        if maximum_revenue_for_range[a][b] == 0:
            # item1 = coins[a] + sum_coins(a + 1, b) - helper(a + 1, b)
            # item2 = coins[b] + sum_coins(a, b - 1) - helper(a, b - 1)
            item1 = coins[a] + min(helper(a + 2, b), helper(a + 1, b - 1))
            item2 = coins[b] + min(helper(a + 1, b - 1), helper(a, b - 2))
            maximum_revenue_for_range[a][b] = max(item1, item2)
        return maximum_revenue_for_range[a][b]
    
    maximum_revenue_for_range = [[0] * len(coins) for _ in coins]
    return helper(0, len(coins) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
