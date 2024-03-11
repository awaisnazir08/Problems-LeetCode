class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = {}
        for element in nums:
            if element not in my_dict:
                my_dict[element] = 1
            else:
                my_dict[element] +=1
        for key, value in my_dict.items():
            if value == 1:
                return key
        