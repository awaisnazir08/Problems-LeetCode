class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def isNoZero(num):
            while num != 0:
                r = num % 10
                if not r:
                    return False
                num //= 10
            return True
            
        for i in range(1, n):
            j = n - i
            if isNoZero(i) and isNoZero(j):
                return [i, j]