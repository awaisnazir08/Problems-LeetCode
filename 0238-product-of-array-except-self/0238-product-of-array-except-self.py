class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = 1
        flag = 0
        for element in nums:
            if element != 0:
                result = result * element
            else:
                if(flag < 2):
                    flag +=1
        
        output = []

        if flag == 2:
            output = [0] * len(nums)
        elif flag == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    output.append(result)
                else:
                    output.append(0)
        else:
            for i in range(len(nums)):
                output.append(result / nums[i])

        return output
