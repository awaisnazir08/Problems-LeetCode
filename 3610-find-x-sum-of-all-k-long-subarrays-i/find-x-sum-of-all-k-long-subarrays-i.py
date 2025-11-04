import heapq

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        freq = {}

        for i in range(k):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        top_k = heapq.nlargest(x, freq.items(), key=lambda e: (e[1], e[0]))

        res = []
        current = 0
        for item in top_k:
            current += (item[0] * item[1])
        res.append(current)
            
        for i in range(k, len(nums)):
            current = 0
            freq[nums[i-k]] -= 1
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            top_k = heapq.nlargest(x, freq.items(), key=lambda e: (e[1], e[0]))
            for item in top_k:
                current += (item[0] * item[1])
            res.append(current)
             
        return res




        