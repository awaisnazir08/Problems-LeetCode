class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        map = {}

        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        m_f = max(map.values())

        res = 0
        for key, val in map.items():
            if val == m_f:
                res += m_f
        
        return res

        