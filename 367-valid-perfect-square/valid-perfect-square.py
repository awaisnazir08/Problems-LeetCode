class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        mark = num // 2
        i = 0
        j = mark
        while i != j:
            if i - j == 1 or i - j == -1:
                if i * i == num or j * j == num:
                    return True
                else:
                    return False
            if i * i == num:
                return True
            elif j * j == num:
                return True
            elif i * i < num:
                i = (i + j) // 2
            elif j * j > num:
                if i * i > num:
                    j = i
                    i = 0
                    continue
                j = (i + j ) // 2

        return False
        