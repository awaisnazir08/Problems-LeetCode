class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = nums[:]

        if not nums:
            return 0
        if n < 3:
            return max(nums)
        for i in range(n - 3):
            if dp[i + 2] < dp[i] + nums[i + 2]:
                dp[i + 2] = dp[i] + nums[i + 2]
            if dp[i + 3] < dp[i] + nums[i + 3]:
                dp[i + 3] = dp[i] + nums[i + 3]
        # last_index = n - 3
        if dp[n - 1] < dp[n - 3] + nums[n - 1]:
            dp[n - 1] = dp[n - 3] + nums[n - 1]
        return max(dp)
            

        