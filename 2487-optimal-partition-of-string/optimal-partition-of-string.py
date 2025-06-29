class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """

        partitions = 0
        map = {}

        for element in s:
            if element not in map:
                map[element] = 1
            else:
                partitions += 1
                map = {}
                map[element] = 1
        if map:
            partitions += 1
        
        return partitions
        