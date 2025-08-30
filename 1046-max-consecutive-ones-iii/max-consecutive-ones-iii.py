class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = 0
        left = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                res = max(res, right - left + 1)
            if nums[right] == 0:
                count += 1
            if count <= k:
                res = max(res, right - left + 1)
            else:
                while count > k:
                    if nums[left] == 0:
                        count -= 1
                    left += 1
        
        return res
                

        