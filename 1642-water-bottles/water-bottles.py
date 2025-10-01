class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        
        drink = 0
        current_empty = 0
        current_filled = numBottles

        while True:
            drink += current_filled
            current_empty += current_filled
            if current_empty < numExchange:
                return drink

            current_filled = int(current_empty / numExchange)
            current_empty = current_empty % numExchange



        