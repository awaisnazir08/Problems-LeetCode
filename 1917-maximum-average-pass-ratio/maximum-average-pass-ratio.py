import heapq
class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        heap = []
        average = 0

        def gain(p, t):
            return ((p + 1) * 1.0 / (t + 1)) - (p * 1.0 /t)

        for clss in classes:
            heapq.heappush(heap, (-gain(clss[0], clss[1]), clss))
        
        for s in range(extraStudents):
            _, clss = heapq.heappop(heap)
            heapq.heappush(heap, (-gain(clss[0] + 1, clss[1] + 1), [clss[0] + 1, clss[1] + 1]))
        
        while heap:
            _, clss = heapq.heappop(heap)
            average += (clss[0] * 1.0 / clss[1])
        
        return average / len(classes)

        

        