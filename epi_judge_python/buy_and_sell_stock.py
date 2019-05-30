from test_framework import generic_test


def buy_and_sell_stock_once(A):
    # TODO - you fill in here.
    maxsofar = 0
    min_item = A[0]
    for i in range(1, len(A)):
    	maxsofar = max(maxsofar, A[i] - min_item)
    	min_item = min(min_item, A[i])
    return maxsofar


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
