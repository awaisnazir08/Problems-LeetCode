class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = 0

        # fix the largest side (k), and find pairs (i, j)
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # all values between i and j will form valid triangles
                    res += (j - i)
                    j -= 1
                else:
                    i += 1

        return res
    