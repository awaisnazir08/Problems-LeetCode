class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        drink = numBottles
        empty = numBottles
        current_filled = 0

        while True:
            while empty >= numExchange:
                empty -= numExchange
                numExchange += 1
                current_filled += 1
            
            drink += current_filled
            empty += current_filled
            current_filled = 0

            if empty < numExchange:
                return drink
        