class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k - 1
        sum = 0
        while r >= 0:
            sum += nums[r]
            r -= 1
        res = sum
        for i in range(k, len(nums)):
            sum += nums[i]
            sum -= nums[l]
            l += 1
            res = max(res, sum)
        

        return res / k

