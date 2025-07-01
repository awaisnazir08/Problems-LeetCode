class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        greatest = nums[0]
        greatest_so_far = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < greatest:
                left = i
                greatest = max(greatest, greatest_so_far)
            greatest_so_far = max(greatest_so_far, nums[i])
        
        return left + 1

        