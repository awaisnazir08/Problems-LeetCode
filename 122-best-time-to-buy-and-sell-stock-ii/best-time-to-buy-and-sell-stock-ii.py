class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        total_profit = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            sell = prices[i]
            max_profit = max(max_profit, sell - buy)
            if sell <= buy:
                buy = sell
            elif sell > buy:
                total_profit += (max_profit)
                buy = sell
                max_profit = 0
        
        return total_profit
