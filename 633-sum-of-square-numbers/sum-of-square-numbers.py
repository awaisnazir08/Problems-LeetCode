class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        squareroot = set()
        for i in range(int(sqrt(c)) + 1):
            squareroot.add(i * i)
        
        for a in range(int(sqrt(c)) + 1):
            if c - a * a in squareroot:
                return True
        return False