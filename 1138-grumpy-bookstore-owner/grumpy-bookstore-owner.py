import numpy as np
class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """

        customers = np.array(customers)
        grumpy = np.array(grumpy)
        existing = sum(customers[grumpy==0])

        current = 0

        l = 0
        r = 0

        for r in range(minutes):
            if grumpy[r] == 1:
                current += customers[r]
        
        gain = current
        
        for r in range(minutes, len(grumpy)):
            if grumpy[l] == 1:
                current -= customers[l]
            
            if grumpy[r] == 1:
                current += customers[r]
            
            l += 1

            gain = max(current, gain)
        
        return existing + gain
        
        