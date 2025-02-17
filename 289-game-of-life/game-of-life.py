class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """


        rows = len(board)
        columns = len(board[0])

        def isValidElement(i, j):
            if (i < 0) or i > (rows - 1) or (j < 0) or (j > columns - 1):
                return False
            return True
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == 1:
                    n_lives = 0

                    for direction in directions:
                        to_check_i = i + direction[0]
                        to_check_j = j + direction[1]

                        if not isValidElement(to_check_i, to_check_j):
                            continue
                        
                        if board[to_check_i][to_check_j] == 1 or board[to_check_i][to_check_j] == 2:
                            n_lives += 1
                    
                    if not (n_lives == 2 or n_lives == 3):
                        board[i][j] = 2
                
                elif board[i][j] == 0:
                    n_lives = 0

                    for direction in directions:
                        to_check_i = i + direction[0]
                        to_check_j = j + direction[1]

                        if not isValidElement(to_check_i, to_check_j):
                            continue
                        
                        if board[to_check_i][to_check_j] == 1 or board[to_check_i][to_check_j] == 2:
                            n_lives += 1
                    
                    if n_lives == 3:
                        board[i][j] = 3
        
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
            





        