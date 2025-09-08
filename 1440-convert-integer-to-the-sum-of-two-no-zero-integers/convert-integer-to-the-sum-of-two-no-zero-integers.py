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
        
        b = n - 1
        for i in range(1, n):
            
            if isNoZero(i) and isNoZero(b):
                return [i, b]
            b -= 1