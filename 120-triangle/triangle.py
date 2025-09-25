class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = []
        dp.append(triangle[0])

        for row in triangle[1:]:
            next = []
            for i in range(len(row)):
                if i == 0:
                    next.append(dp[-1][0] + row[i])
                elif i == len(row) - 1:
                    next.append(dp[-1][i - 1] + row[i])
                else:
                    next.append(min(dp[-1][i] + row[i], dp[-1][i - 1] + row[i]))
            dp.append(next)
    
        return min(dp[-1])


        