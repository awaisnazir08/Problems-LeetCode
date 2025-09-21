class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1
        c = int((l + r) / 2)
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                c = i - 1
                break
        
        if nums[c] == target:
            return c

        if nums[l] <= target <= nums[c]:
            l = l
            r = c - 1
            c = (l + r) // 2
        else:
            l = c + 1
            c = (l + r) // 2
            r = r
        
        if nums[c] == target:
            return c

        while l <= r:
            c = (l + r) // 2
            if nums[c] == target:
                return c
            
            if target < nums[c]:
                r = c - 1
            else:
                l = c + 1
        
        return -1
        



