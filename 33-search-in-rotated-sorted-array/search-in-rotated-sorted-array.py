class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(left, center, right):
            if left == right:
                return left if nums[left] == target else -1
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[center] == target:
                return center
            elif nums[left] < target < nums[center]:
                return binarySearch(left, int((left + center) / 2), center)
            else:
                return binarySearch(min(right, center + 1), int((center + 1 + right) / 2), right)

        l = 0
        r = len(nums) - 1
        c = int((l + r) / 2)
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                c = i - 1
                break
        
        if nums[c] == target:
            return c

        if nums[l] <= target <= nums[c]:
            return binarySearch(l, int((l + c)/2), c)
        else:
            return binarySearch(min(r, c + 1), int((c + 1 + r)/2), r)

