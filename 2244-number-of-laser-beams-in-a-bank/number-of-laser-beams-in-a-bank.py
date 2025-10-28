class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """

        res = 0

        left = 0

        while left < len(bank):
            row = bank[left]

            l_ones = row.count('1')

            if l_ones > 0:
                break
            left += 1
        
        for r in range(left + 1, len(bank)):
            r_ones = bank[r].count('1')
            if r_ones > 0:
                res += (l_ones * r_ones)
                left = r
                l_ones = r_ones
        
        return res


        