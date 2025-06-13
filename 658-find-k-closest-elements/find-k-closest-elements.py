import heapq
from itertools import count
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        que = []
        counter = count()
        for element in arr:
            heapq.heappush(que, (abs(element - x), next(counter), element))
        res = []
        for i in range(k):
            freq, _, element = heapq.heappop(que)
            res.append(element)
        res.sort()
        return res