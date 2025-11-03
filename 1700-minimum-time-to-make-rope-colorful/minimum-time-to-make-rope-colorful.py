class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """

        n = len(colors)

        current = neededTime[0]

        res = 0

        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                res += min(current, neededTime[i])
                current = max(current, neededTime[i])
            else:
                current = neededTime[i]
        
        return res
                


                
        