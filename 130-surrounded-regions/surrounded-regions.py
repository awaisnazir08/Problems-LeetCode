from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        rows = len(board)
        columns = len(board[0])
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            board[r][c] = 'S'
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if 0 <= nr < rows and 0 <= nc < columns and (nr, nc) not in visited and board[nr][nc] == 'O':
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        board[nr][nc] = 'S'


        for i in range(0, columns):
            if board[0][i] == 'O' and (0, i) not in visited:
                bfs(0, i)
            if board[rows - 1][i] == 'O' and (rows -1, i) not in visited:
                bfs(rows - 1, i)
        
        for i in range(0, rows):
            if board[i][0] == 'O' and (i, 0) not in visited:
                bfs(i, 0)
            if board[i][columns - 1] == 'O' and (i, columns - 1) not in visited:
                bfs(i, columns - 1)
        
        
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'

