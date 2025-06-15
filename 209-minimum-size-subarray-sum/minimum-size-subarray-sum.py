class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        sum = 0
        length = float('inf')
        for r in range(len(nums)):
            sum += nums[r]
            if sum < target:
                continue
            else:
                while sum >= target:
                    current_length = r - l + 1
                    length = min(length, current_length)
                    sum -= nums[l]
                    l += 1
        return 0 if length == float('inf') else length


