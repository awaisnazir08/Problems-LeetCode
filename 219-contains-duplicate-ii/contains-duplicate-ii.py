class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}

        loc = {}

        for i, num in enumerate(nums):
            if num not in freq:
                freq[num] = 0
                loc[num] = i
            freq[num] += 1

            if freq[num] > 1:
                if abs(loc[num] - i) <= k:
                    return True
                else:
                    loc[num] = i
        
        return False

