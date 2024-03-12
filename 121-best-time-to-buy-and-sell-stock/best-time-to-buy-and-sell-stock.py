class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 1 or n == 0:
            return 0
        
        profit = 0
        buy_price = 0
        for sell_price in range(1, n):
            if prices[sell_price] > prices[buy_price]:
                new_profit = prices[sell_price] - prices[buy_price]
                profit = max(profit, new_profit)
            else:
                buy_price = sell_price
        return profit

        