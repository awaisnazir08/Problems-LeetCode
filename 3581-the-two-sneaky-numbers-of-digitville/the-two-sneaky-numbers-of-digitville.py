class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        res = []

        for num in nums:
            if num in s:
                res.append(num)
            else:
                s.add(num)
        return res