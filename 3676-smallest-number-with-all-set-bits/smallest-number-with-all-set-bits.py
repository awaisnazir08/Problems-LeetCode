class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = n
        while True:
            bc = bin(c)[2:]
            if bc.count('0') == 0:
                return c
            c += 1
        