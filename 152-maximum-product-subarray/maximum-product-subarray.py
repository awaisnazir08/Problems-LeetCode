class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # my_dict = {}
        # i = 0, j = 1
        n = len(nums)
        # for i in range(0, n):
        #     for j in range(i, n):
        #         if my_dict[ij] in my_dict:

        # product = 0
        # if len(nums) == 1:
        #     return nums[0]
        # j = nums[1]
        # for i in nums[1:]:
        #     new_product = i * j
        max_product = float('-inf')
        product = 1
        if n == 1:
            return nums[0]
        for i in range(n):
            if nums[i] ==0:
                product = 1
                continue
            product *= nums[i]
            # if(product == 0):
            #     product = 1
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
            



        