class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        middle = (i + j) // 2
        while i != j:
            if i - j == 1 or i - j == -1:
                if nums[i] < nums[j]:
                    return nums[i]
                else:
                    return nums[j]
            if nums[i] > nums[j]:
                if i > 0 and nums[i - 1 ] < nums[i] and nums[i - 1] < nums[j]:
                        j = (i + j) // 2
                        continue
                i = (i + j) // 2
            else:
                if i > 0 and nums[i - 1 ] < nums[i] and nums[i - 1] < nums[j]:
                        j = i
                        i = 0
                        continue
                j = (i + j) // 2
        return nums[i]

        