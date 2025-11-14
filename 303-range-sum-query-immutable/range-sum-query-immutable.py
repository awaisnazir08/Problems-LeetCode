class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.prefix_sum = []
        self.prefix_sum.append(nums[0])
        for i in range(1, len(nums)):
            self.prefix_sum.append(nums[i] + self.prefix_sum[i - 1])    

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left > 0:
            return self.prefix_sum[right] - self.prefix_sum[left - 1]
        else:
            return self.prefix_sum[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)