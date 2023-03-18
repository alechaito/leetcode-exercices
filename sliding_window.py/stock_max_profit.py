prices = [7,1,5,3,6,4]

def get_max_profit(prices):
    max_profit = 0
    lowest = prices[0]

    for price in prices:
        if price < lowest:
            lowest = price

        max_profit = max(max_profit, price-lowest)

    return max_profit

print(get_max_profit(prices))
""" 
trick: need to move the pointer to the low value founded to maximize the profit
finding the lowest value you will always try to find the max profit computing
actual price and lowest value founded that will give use the maximum profit possible
"""