class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest_sequence = 0
        for i in numSet:
            if (i - 1) not in numSet:
                length = 0
                while(i + length) in numSet:
                    length += 1
                longest_sequence = max(length, longest_sequence)
        return longest_sequence
    
        