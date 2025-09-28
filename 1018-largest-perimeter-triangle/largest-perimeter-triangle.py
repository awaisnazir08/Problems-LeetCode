class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        for i in range(n - 1, 1, -1):
            if nums[i - 1] + nums[i - 2] > nums[i]:
                return nums[i - 1] + nums[i - 2] + nums[i]
        
        return 0
        