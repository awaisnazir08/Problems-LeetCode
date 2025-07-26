from collections import deque
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        visited = set()

        rows = len(board)
        columns = len(board[0])
        ships = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def cover_ship(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                r, c = q.popleft()
                for row, col in directions:
                    nr = r + row
                    nc = c + col
                    if 0 <= nr < rows and 0 <= nc < columns and board[nr][nc] == 'X' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == 'X' and (i, j) not in visited:
                    cover_ship(i, j)
                    ships += 1
        

        return ships

        