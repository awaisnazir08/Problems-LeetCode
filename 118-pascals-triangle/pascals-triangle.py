class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            new = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    new.append(1)
                else:
                    new.append(triangle[i - 1][j-1] + triangle[i - 1][j])
            triangle.append(new)

        return triangle


        