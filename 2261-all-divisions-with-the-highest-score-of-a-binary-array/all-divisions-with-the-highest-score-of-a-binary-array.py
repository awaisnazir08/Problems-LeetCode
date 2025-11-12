class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        map = {0: 0, 1: 0}

        scores = []

        for num in nums:
            map[num] += 1

        n = len(nums)
        left = 0
        right = map[1]

        scores.append(right)

        for i in range(n):
            if nums[i] == 0:
                left += 1
                scores.append(left + right)
            elif nums[i] == 1:
                right -= 1
                scores.append(left + right)
        
        max_value = max(scores)

        indices = [i for i, x in enumerate(scores) if x == max_value]
        return indices
        