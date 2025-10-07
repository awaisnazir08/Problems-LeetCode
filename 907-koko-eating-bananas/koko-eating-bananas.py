import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left, right = 1, max(piles)
        res = right

        while left <= right:
            middle = (left + right) // 2
            current_hours = 0

            for pile in piles:
                current_hours += math.ceil(pile / float(middle))
                if current_hours > h: 
                    break

            if current_hours <= h:
                res = middle
                right = middle - 1
            else:
                left = middle + 1

        return res
