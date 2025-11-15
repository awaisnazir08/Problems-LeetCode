class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        seen_at = {}
        seen_at[0] = -1
        res = 0

        for i, num in enumerate(nums):
            count += 1 if num else -1

            if count not in seen_at:
                seen_at[count] = i
            else:
                res = max(res, i - seen_at[count])
                # don't update the seen_at because we want the global, not local minimum
                # updating it will give us as close to the current index as possible, decreasing the length of the subarray, which is not what we want

        return res
            
