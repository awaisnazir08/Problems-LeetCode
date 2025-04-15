class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        binary_ones = []

        for item in arr:
            binary_ones.append(bin(item)[2:].count('1'))
        
        combined = list(zip(arr, binary_ones))
        combined.sort(key = lambda x: x[1])

        j = 0
        to_return = []
        while j < len(arr):
            current = combined[j][1]
            temp = []
            while j < len(arr) and current == combined[j][1]:
                temp.append(combined[j][0])
                j += 1
            temp.sort()
            to_return += temp
        
        return to_return
        