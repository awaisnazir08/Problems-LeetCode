class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        greatest_num = nums[-1]
        if len(nums) == 0:
            return []
        current = nums[0]
        to_start = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == current:
                count += 1
                if count > 2:
                    to_start = i
                    break
            else:
                count = 1
                current = nums[i]
        
        positions = {}
        to_keep = {}
        total = 0
        for i in range(len(nums)):
            if nums[i] not in positions:
                positions[nums[i]] = i
            if nums[i] not in to_keep:
                to_keep[nums[i]] = 1
                total += 1
            else:
                if to_keep[nums[i]] < 2:
                    to_keep[nums[i]] += 1
                    total += 1

        i = to_start
        while i < len(nums):
            j = nums[i - 1] + 1
            while j not in positions:
                j += 1
                if j > greatest_num:
                    break
            if j > greatest_num:
                break    
            k = positions[j]
            while to_keep[j] > 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
                i += 1
                to_keep[j] -= 1
            
        return total


