class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)

        for i, num in enumerate(nums):
            if num == val:
                nums[i] = 1000
                n -= 1
        nums.sort()
        return n
            

        