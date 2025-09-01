import heapq
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        res = []
        max_element = -heap[0][0]
        m_idx = heap[0][1]
        res.append(max_element)
        
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if nums[i] > max_element:
                max_element = nums[i]
                m_idx = i
                res.append(max_element)
            elif m_idx > i - k:
                res.append(max_element)
            else:
                while m_idx <= i - k:
                    max_element, m_idx = heapq.heappop(heap)
                    max_element = -max_element
                res.append(max_element)
        
        return res

            