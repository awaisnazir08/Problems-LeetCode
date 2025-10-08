class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for spell in spells:
            left = 0
            right = len(potions) - 1

            while left <= right:
                middle = (left + right) // 2

                if potions[middle] * spell >= success:
                    right = middle - 1
                else:
                    left = middle + 1
            if potions[middle] * spell >= success:
                res.append(len(potions) - middle)
            else:
                res.append(len(potions) - middle - 1)
        
        return res
                
        