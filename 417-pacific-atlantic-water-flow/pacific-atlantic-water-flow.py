
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        pacific, atlantic = set(), set()
        rows, cols = len(heights), len(heights[0])

        def bfs(row, col, visit, element):
            my_queue = [(row, col, element)]
            # visit.add((row, col))
            while my_queue:
                current = my_queue.pop(0)
                row, col, value = current
                if (row < 0 or col < 0 or row == rows or col == cols or (row, col) in visit):
                    continue
                else:
                    visit.add((row, col))
                    if row + 1 < rows and heights[row + 1][col] >= value:
                        my_queue.append((row + 1, col, heights[row + 1][col]))
                    if row - 1 >= 0 and heights[row - 1][col] >= value:
                        my_queue.append((row - 1, col, heights[row - 1][col]))
                    if col + 1 < cols and heights[row][col + 1] >= value:
                        my_queue.append((row, col + 1, heights[row][col + 1]))
                    if col - 1 >= 0 and heights[row][col - 1] >= value:
                        my_queue.append((row, col - 1, heights[row][col - 1]))


        for row in range(rows):
            bfs(row, 0, pacific, heights[row][0])
            bfs(row, cols - 1, atlantic, heights[row][cols - 1])

        for col in range(cols):
            bfs(0, col, pacific, heights[0][col])
            bfs(rows - 1, col, atlantic, heights[rows - 1][col])

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        return result