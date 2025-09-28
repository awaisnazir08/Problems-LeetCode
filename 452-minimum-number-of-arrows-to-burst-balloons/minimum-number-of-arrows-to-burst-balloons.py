class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points.sort(key = lambda x: x[0])

        res = []
        res.append(points[0])
        
        for point in points[1:]:
            last = res[-1]

            if point[0] <= last[1]:
                last[0] = max(point[0], last[0])
                last[1] = min(point[1], last[1])
            else:
                res.append(point)
        
        return len(res)