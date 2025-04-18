class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        # for i in range(k):
        #     last = nums[-1]
        #     for j in range(len(nums) - 1, 0, -1):
        #         nums[j] = nums[j - 1] 
        #     nums[0] = last
        i = 0
        current_element = nums[i]
        unique = set()
        # unique.add(i)
        # new_position = (i + k) % len(nums)
        # current_element = nums[new_position]
        # nums[new_position] = nums[i]

        while True:
            new_position = (i + k) % len(nums)
            if new_position not in unique:
                next_element = nums[new_position]
                nums[new_position] = current_element
                current_element = next_element
                i = new_position
                unique.add(i)
            elif len(unique) == len(nums):
                break
            else:
                for j in range(len(nums)):
                    if j not in unique:
                        i = j
                        current_element = nums[i]

