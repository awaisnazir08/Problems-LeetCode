class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(node, path, visited):
            if len(path) == len(word):
                return True
            r, c = node[0], node[1]
            for dr, dc in directions:
                row = dr + r
                col = dc + c
                if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited:
                    if word[len(path)] == board[row][col]:
                        path.append(board[row][col])
                        visited.add((row, col))
                        if dfs((row, col), path, visited):
                            return True
                        visited.remove((row, col))
                        path.pop(0)
            
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs((i, j), [board[i][j]], {(i, j)}):
                        return True
        
        return False




                
        