import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        res = []
        for row in matrix:
            res.extend(row)
        
        res.sort()

        return res[k-1]
        