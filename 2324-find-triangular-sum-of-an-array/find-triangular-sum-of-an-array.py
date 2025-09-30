class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1 - i):
                nums[j] = (nums[j] + nums[j + 1]) % 10
        
        return nums[0]

        