class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 1 or not nums:
            return 0
        l = 0 
        result = 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > 1:
                l += 1
            
            if nums[r] - nums[l] == 1:
                result = max(result, r - l + 1)
        
        return result


