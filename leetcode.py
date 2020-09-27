import copy


def maxProfit(prices):
    s1 = copy.deepcopy(prices)
    s1.sort(reverse=True)
    if prices == s1:
        return 0
    min_price = min(prices)
    index = prices.index(min_price)
    max_price = max(prices[index:])
    return max_price - min_price


max_profit = maxProfit([2, 4, 1])
print(max_profit)
