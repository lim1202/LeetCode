'''Best Time to Buy and Sell Stock'''
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction
# (ie, buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.


def max_profit1(prices):
    '''Caculate max profit at one transaction'''
    days = len(prices)
    if days <= 1:
        return 0

    min_p = prices[0]
    profit = prices[1] - prices[0]

    for i in range(days):
        if i <= 1:
            continue

        min_p = min(prices[i - 1], min_p)
        profit = max(profit, prices[i] - min_p)

    if profit < 0:
        return 0

    return profit


# Best Time to Buy and Sell Stock II
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).


def max_profit2(prices):
    '''Caculate max profit at multi transactions'''
    days = len(prices)
    if days <= 1:
        return 0

    sum_profit = 0
    for i in range(days):
        if prices[i] - prices[i - 1] > 0:
            sum_profit = sum_profit + prices[i] - prices[i - 1]

    return sum_profit


# Best Time to Buy and Sell Stock III
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit.
# You may complete at most two transactions.
# Note: You may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).


def max_profit3(prices):
    '''Caculate max profit at two transactions'''
    days = len(prices)
    if days <= 1:
        return 0

    profits = [0 for i in range(days)]

    # forward
    min_p = prices[0]
    sum_profit = 0
    for i in range(days):
        if i == 0:
            continue

        min_p = min(min_p, prices[i - 1])
        profits[i] = max(sum_profit, prices[i] - min_p)

        sum_profit = profits[i]

    max_p = prices[-1]
    sum_profit2 = 0

    # backward
    rev = [i for i in range(days)]
    rev.reverse()
    for i in rev:
        if i == days - 1:
            continue

        max_p = max(max_p, prices[i + 1])
        sum_profit2 = max(sum_profit2, max_p - prices[i])

        if sum_profit2 > 0:
            profits[i] = profits[i] + sum_profit2
            sum_profit = max(sum_profit, profits[i])

    if sum_profit < 0:
        sum_profit = 0

    return sum_profit


if __name__ == '__main__':
    PRICES = [
        1015.8,
        1022.37,
        1042.68,
        1055.09,
        1040,
        1035.87,
        1035,
        1023.31,
        1020.26,
        1034.01,
        1022.52,
        1019.21,
        1022.59,
        1023.42,
        1026.46,
        1033.99,
        1030.52,
        1027.27,
        1028.99,
        1022.11,
        1021.76,
        1017.2]

    print('Google stock:', PRICES)
    print('max profit 1:', max_profit1(PRICES))
    print('max profit 2:', max_profit2(PRICES))
    print('max profit 3:', max_profit3(PRICES))
