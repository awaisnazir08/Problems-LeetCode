class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getIndexes(c):
            start = c
            end = c
            while c >= 0 and nums[c] == target:
                start = c
                c -= 1
            
            c = end
            while c < len(nums) and nums[c] == target:
                end = c
                c += 1
            
            return [start, end]
        
        def binarySearch(l, c, r):
            if r - l == 0 and nums[c] == target:
                return getIndexes(c)
            elif r - l == 0 and nums[c] != target:
                return [-1, -1]
            elif nums[c] == target:
                return getIndexes(c)
            elif target < nums[c]:
                r = c
                return binarySearch(l, int((l + r) / 2), r)
            else:
                l = c + 1
                c = int((l + r) / 2)
                return binarySearch(l, c, r)

        if len(nums) == 0:
            return [-1, -1]
            
        center = int(len(nums) / 2)

        if nums[center] == target:
            return getIndexes(center)
        elif target < nums[center]:
            left = 0
            right = center
            center = int((left + right) / 2)
            return binarySearch(left, center, right)
        else:
            left = center + 1
            right = len(nums) - 1
            center = int((left + right) / 2)
            return binarySearch(min(left, right), center, right)
