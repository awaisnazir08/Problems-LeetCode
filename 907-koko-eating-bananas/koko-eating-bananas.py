import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        highest = max(piles)

        left = 1
        right = highest

        res = right

        while left <= right:
            middle = (left + right) // 2

            current_hours = 0

            for pile in piles:
                current_hours += int(math.ceil(pile / float(middle)))

                if current_hours > h:
                    left = middle + 1
                    break


            if current_hours <= h:
                res = min(res, middle)

                right = middle - 1

        return int(res)