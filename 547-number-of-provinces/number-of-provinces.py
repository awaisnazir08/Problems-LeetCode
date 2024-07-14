# import queue
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        #  1  2  3
        # 1[1,1,0]
        # 2[1,1,0]
        # 3[0,0,1]
        q = []
        provinces = 0
        visited = set()
        for i in range(len(isConnected)):
            if i in visited:
                continue
            visited.add(i)
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1 and j not in visited:
                    q.append(j)
            while q:
                k = q.pop(0)
                for l in range(len(isConnected[0])):
                    if k != l and isConnected[k][l] == 1 and l not in visited and k not in visited:
                        q.append(l)
                visited.add(k)
            provinces += 1
        return provinces
            




        