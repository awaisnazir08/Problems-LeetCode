class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        j = 0
        sum = 0
        atmost_g = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum <= goal:
                atmost_g += (i - j + 1)
            else:
                while j < i and sum > goal:
                    sum -= nums[j]
                    j += 1
                if sum <= goal:
                    atmost_g += (i - j + 1)
        
        atmost_g_minus_1 = 0
        j = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum <= (goal - 1):
                atmost_g_minus_1 += (i - j + 1)
            else:
                while j < i and sum > (goal - 1):
                    sum -= nums[j]
                    j += 1
                if sum <= goal - 1:
                    atmost_g_minus_1 += (i - j + 1)
        return atmost_g - atmost_g_minus_1




        
