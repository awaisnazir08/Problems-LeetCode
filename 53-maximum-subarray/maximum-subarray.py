class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        max_sum = float('-inf')
        sum = 0
        for i in range(n):
            sum += nums[i]
            if sum < 0:
                sum = 0
            max_sum = max(sum, max_sum)
        if max(nums) < 0:
            return max(nums)
        return max_sum