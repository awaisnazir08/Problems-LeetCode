class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_dict = {}
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                return True
        return False
        