class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            return 1
        
        left, right = 1, n // 2
        res = 0

        def is_valid(k: int) -> bool:
            if k == 1:
                return True
            count = 0
            for i in range(n - k - 1):
                if nums[i] < nums[i + 1] and nums[i + k] < nums[i + k + 1]:
                    count += 1
                    if count >= k - 1:
                        return True
                else:
                    count = 0
            return False

        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                res = max(mid, res)
                left = mid + 1
            else:
                right = mid - 1

        return res
