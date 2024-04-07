class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # k = n - k
        # def quickSelect(p, r):
        #     # lb = r
        #     x = nums[r]
        #     i = p - 1
        #     for j in range(p, r):
        #         if(nums[j]<=x):
        #             i = i + 1
        #             nums[i], nums[j] = nums[j], nums[i]
        #     nums[i+1], nums[r] = nums[r], nums[i + 1]
        #     if (i + 1) > k: return quickSelect(p, i)
        #     elif i + 1 < k: return quickSelect(i+2, r)
        #     else: return nums[i + 1]
        
        # return quickSelect(0, n-1)

        nums.sort()
        return nums[n-k]

                