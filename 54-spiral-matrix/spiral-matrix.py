class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        rotations = {
            'start_row': 0,
            'end_row': m - 1,
            'start_column': 0,
            'end_column': n - 1
        }

        turn = 0
        output_matrix = []

        while (True):
            new_element_added = False
            if turn == 0:
                for i in range(rotations['start_column'], rotations['end_column'] + 1):
                    output_matrix.append(matrix[rotations['start_row']][i])
                    new_element_added = True
                if rotations['start_row'] < m - 1:
                    rotations['start_row'] += 1
            
            elif turn == 1:
                for i in range(rotations['start_row'], rotations['end_row'] + 1):
                    output_matrix.append(matrix[i][rotations['end_column']])
                    new_element_added = True
                if rotations['end_column'] > 0:
                    rotations['end_column'] -= 1
            
            elif turn == 2:
                for i in range(rotations['end_column'], rotations['start_column'] - 1, -1):
                    output_matrix.append(matrix[rotations['end_row']][i])
                    new_element_added = True
                if rotations['end_row'] > 0:
                    rotations['end_row'] -= 1
            
            elif turn == 3:
                for i in range(rotations['end_row'], rotations['start_row'] - 1, -1):
                    output_matrix.append(matrix[i][rotations['start_column']])
                    new_element_added = True
                if rotations['start_column'] < n - 1:
                    rotations['start_column'] += 1
            
            if not new_element_added or (len(output_matrix) == m * n):
                break
            
            turn = (turn + 1) % 4

        return output_matrix
