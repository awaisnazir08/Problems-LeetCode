class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """

        n = len(colors)

        l = 0

        r = 0
        res = 0

        current = 0
        while r < n:
            if colors[r] == colors[l]:
                current = max(neededTime[l], neededTime[r], current)
                res += neededTime[r]
            else:
                res -= current
                l = r
                current = 0
                current = max(neededTime[l], neededTime[r])
                res += neededTime[r]
            r += 1
        
        return res - current


                
        