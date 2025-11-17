class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        left = -1

        for r in range(len(nums)):
            if nums[r]:
                if left == -1:
                    left = r
                    continue
                else:
                    if r - left - 1 < k:
                        return False
                    left = r
        
        return True

        