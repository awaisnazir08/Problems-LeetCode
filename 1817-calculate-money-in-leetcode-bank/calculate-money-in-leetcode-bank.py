class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """

        res = 0

        current = 0
        for i in range(n):
            if i % 7 == 0:
                current += 1
                other = current + 1
                res += current
            else:
                res += other 
                other += 1
        
        return res


        