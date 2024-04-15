class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        my_dict = { 0: 1
        }
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            diff = sum - k
            if diff in my_dict:
                result += my_dict[diff]
            if sum in my_dict:
                my_dict[sum] += 1
            else:
                my_dict[sum] = 1
        return result
            
        