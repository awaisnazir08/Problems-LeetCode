class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        power = 1
        while 2 ** power <= n:
            power += 1
        return 2 ** power - 1
        