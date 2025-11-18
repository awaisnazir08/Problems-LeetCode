class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        previous = False
        res = False
        for i, bit in enumerate(bits):
            if bit == 1 and previous:
                res = True
                previous = False
            elif bit == 1 and not previous:
                previous = True
                res = False
            elif bit == 0 and previous:
                res = False
                previous = False
            elif bit == 0 and not previous:
                res = True
        
        return res


        