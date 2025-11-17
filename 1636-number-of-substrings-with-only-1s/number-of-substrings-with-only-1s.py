class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """

        res = 0

        start = False
        l = -1
        current_length = 0
        for r in range(len(s)):
            if s[r] == '1' and not start:
                l = r
                start = True
            elif s[r] == '0':
                if start:
                    current_length = r - l 
                    res += (current_length + 1) * current_length // 2
                    start = False
        
        if start:
            current_length = (len(s) - l)
            res += (current_length + 1) * current_length // 2
        
        return res % (10**9 + 7)

        