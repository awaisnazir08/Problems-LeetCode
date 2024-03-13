class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_product = float('-inf')
        product = 1
        if n == 1:
            return nums[0]
        for i in range(n):
            if nums[i] ==0:
                product = 1
                continue
            product *= nums[i]
            max_product = max(product, max_product)
        j = n - 1
        product = 1
        while j >=0:
            if nums[j] == 0:
                j-= 1
                product = 1
                continue
            product *= nums[j]
            max_product = max(product, max_product)
            j -= 1
        max_element = max(nums)
        if(max_element > max_product):
            max_product = max_element
        return max_product