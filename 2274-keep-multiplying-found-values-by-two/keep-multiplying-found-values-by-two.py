class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        s = set(nums)
        next = original
        while True:
            if next in s:
                next *= 2
            else:
                return next
        