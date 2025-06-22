class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 0
            map[num] += 1
    
        res = []
        for num in nums:
            if map[num] == 1:
                if num - 1 not in map and num + 1 not in map:
                    res.append(num)
        

        return res
