def maxProfit( prices, fee):
    """
    :type prices: List[int]
    :type fee: int
    :rtype: int
    """
    n = len(prices)
    profit = 0 
    eff_buy = prices[0]
    
    for i in range(n):
        if profit < prices[i] - (eff_buy + fee):
            profit = prices[i] - (eff_buy + fee)
        if eff_buy > prices[i] - profit:
            eff_buy = prices[i] - profit
    return profit


print(maxProfit([1,3,2,8,4,9],2))
print(maxProfit([1,4,6,2,8,3,10,14],3))
