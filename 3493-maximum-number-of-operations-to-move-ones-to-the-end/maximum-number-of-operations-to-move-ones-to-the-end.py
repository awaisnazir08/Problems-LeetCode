class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """

        count_ones = 0
        res = 0
        counted_zero_already = False

        for i, ch in enumerate(s):
            if ch == '1':
                count_ones += 1
                counted_zero_already = False
            elif ch == '0':
                if not counted_zero_already:
                    res += count_ones
                counted_zero_already = True
        
        return res

            
        