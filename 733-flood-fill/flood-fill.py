from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]

        rows, columns = len(image), len(image[0])

        if original_color == color:
            return image

        q = deque()

        q.append((sr, sc))

        directions = [(0,1), (-1, 0), (1, 0), (0, -1)]

        while q:
            r, c = q.popleft()
            if image[r][c] == original_color:
                image[r][c] = color

                for direction in directions:
                    row = direction[0]
                    col = direction[1]

                    if 0 <= r + row < rows and 0 <= c + col < columns and image[r + row][c + col] == original_color:
                        q.append((r + row, c + col))
            
        return image
        