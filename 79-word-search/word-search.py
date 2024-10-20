class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row, col = len(board), len(board[0])

        def checkrange(i, j):
            if i < 0 or j < 0:
                return False
            elif (i > row - 1) or (j > col - 1):
                return False
            return True

        def possible_moves(i, j):
            return [(i + 1, j), (i - 1, j), (i, j + 1 ), (i, j - 1)]

        def backtrack(parents):
            if (len(parents) == len(word)):
                return True
            current_i, current_j = parents[-1]
            moves = possible_moves(current_i, current_j)

            for move in moves:
                if move not in parents and checkrange(move[0], move[1]):
                    if board[move[0]][move[1]] == word[len(parents)]:
                        new_parents = parents + [(move)]
                        if backtrack(new_parents):
                            return True


            

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack([(i, j)]):
                        return True
        return False

        