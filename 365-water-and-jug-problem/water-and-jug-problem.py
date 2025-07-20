from collections import deque
class Solution(object):
    def canMeasureWater(self, x, y, target):
        """
        :type x: int
        :type y: int
        :type target: int
        :rtype: bool
        """

        if x + y < target:
            return False

        queue = deque()
        queue.append([0, 0])
        visited = set()
        visited.add((0, 0))

        def transferX(l, r):
            temp = l
            l = min(x, l + r)
            r = r - (l - temp)
            return (l, r)
        
        def transferY(r, l):
            temp = r
            r = min(y, l + r)
            l = l - (r - temp)
            return (l, r)

        while queue:
            l, r = queue.popleft()

            if l + r == target:
                return True
            
            if (0, r) not in visited:
                queue.append([0, l])
                visited.add((0, l))
            
            if (l, 0) not in visited:
                queue.append((l, 0))
                visited.add((l, 0))
            
            if (x, r) not in visited:
                queue.append((x, r))
                visited.add((x, r))
            
            if (l, y) not in visited:
                queue.append((l, y))
                visited.add((l, y))
            
            if l < x and r > 0:
                a, b = transferX(l, r)
                if (a, b) not in visited:
                    queue.append((a, b))
                    visited.add((a, b))
            
            if r < y and l > 0:
                a, b = transferY(r, l)
                if (a, b) not in visited:
                    queue.append((a, b))
                    visited.add((a, b))
        
        return False



            