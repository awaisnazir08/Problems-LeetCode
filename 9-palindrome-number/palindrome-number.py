class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        if temp < 0:
            return False
        elif temp == 0:
            return True
        hmm = []
        while temp > 0:
            e = temp % 10
            temp = temp // 10
            hmm.append(e)
        i = 0
        j = len(hmm) - 1
        while (i < j):
            if(hmm[i] != hmm[j]):
                return False
            else:
                i += 1
                j -= 1
        return True
