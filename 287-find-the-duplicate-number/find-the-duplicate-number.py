class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = {}

        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                return num
        