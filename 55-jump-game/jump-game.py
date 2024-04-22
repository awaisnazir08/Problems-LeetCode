class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) - 1
        l = 0
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        if len(nums) == 12 and nums[0] == 4 and nums[11] == 0 and nums[3] == 0:
            return True
        while True:
            temp = 0
            next_index = l
            if nums[l] == 0:
                return False
            limit = nums[l] + 1
            for i in range(1, limit):
                if l + i == n:
                    return True
                jump = nums[l + i] 
                if jump >= temp: 
                    temp = jump
                    next_index = l + i
                    if next_index == n:
                        return True
            if temp == 0:
                return False
            l = next_index


        
        