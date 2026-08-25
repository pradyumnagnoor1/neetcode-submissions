class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        L, R = 0, ROWS * COLS - 1

        while L <= R:
            m =  L + (R - L) // 2

            row, col = m // COLS, m % COLS

            if target > matrix[row][col]:
                L = m + 1

            elif target < matrix[row][col]:
                R = m - 1

            else:
                return True

        return False

        
                




        