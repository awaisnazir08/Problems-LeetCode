class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        knew = k - 1
        if not knew:
            return True

        for i in range(len(nums) - k - 1):
            if nums[i] < nums[i + 1] and nums[i + k] < nums[i + k + 1]:
                knew -= 1
            else:
                knew = k - 1
            
            if knew == 0:
                return True
        
        return False