import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        res = []

        n = len(nums)

        for key, val in frequency.items():
            if val > math.floor(n/3):
                res.append(key)

        return res
        