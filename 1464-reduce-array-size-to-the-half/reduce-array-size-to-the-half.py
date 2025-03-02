import heapq

class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        map = {}

        heap = []

        n = len(arr)

        for num in arr:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        
        for num, freq in map.items():
            heapq.heappush(heap, -freq)
        
        eliminated_freq = 0
        set_size = 0
        while heap:
            current = heapq.heappop(heap)
            eliminated_freq += (-current)
            set_size += 1

            if eliminated_freq >= (n/2):
                return set_size
        
        return 1


        

        