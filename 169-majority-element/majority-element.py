class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        n = len(nums)
        for num in nums:
            map[num] = map.get(num, 0) + 1

            if map[num] > (n // 2):
                return num
        