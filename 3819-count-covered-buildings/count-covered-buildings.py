class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        map_x = {}
        res = 0
        map_y = {}


        for x, y in buildings:
            if x not in map_x:
                map_x[x] = [(x, y)]
            else:
                map_x[x].append((x, y))
            
            if y not in map_y:
                map_y[y] = [(x, y)]
            else:
                map_y[y].append((x, y))
        
        covered_x = set()
        for key, value in map_x.items():
            value.sort(key=lambda x: x[1])  # why opposite
            value.pop(0)
            if value:
                value.pop(-1)
            covered_x.update(value)
        
        covered_y = set()
        for key, value in map_y.items():
            value.sort(key=lambda x: x[0])
            value.pop(0)
            if value:
                value.pop(-1)
            covered_y.update(value)
        
        return len(covered_x & covered_y)
