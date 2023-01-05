l = 0
r = 1
max_profit = 0
prices = [7,1,5,3,6,4]

def get_max_profit(prices):
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        
        r += 1 
    
    return max_profit

# trick: need to move the pointer to the low value founded to maximize the profit