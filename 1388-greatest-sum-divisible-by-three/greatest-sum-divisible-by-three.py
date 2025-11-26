class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]  # best sums for remainders 0,1,2
        
        for num in nums:
            new_dp = dp[:]  # to avoid in-place update conflict
            for r in range(3):
                candidate = dp[r] + num
                new_dp[int(candidate % 3)] = max(new_dp[int(candidate % 3)], candidate)
            dp = new_dp
        
        return dp[0]
