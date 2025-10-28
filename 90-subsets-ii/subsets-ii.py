class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def backtrack(start, elements):
            if elements not in res:
                res.append(elements[:])
            
            for i in range(start, len(nums)):
                elements.append(nums[i])
                ne = sorted(elements)
                backtrack(i + 1, ne)
                elements.pop()
        
        backtrack(0, [])

        return res


        