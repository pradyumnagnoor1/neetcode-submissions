class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        """O(log n * m) means that I can run binary search twice, I can 
        run it once to find the right row. by comparing target to the 
        max and min value in the mid row"""

        """Once I find the right row I can run regular binary search on 
        the right row and then see if the target exists in the row"""


        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1

        while top <= bottom:
            mid = top + (bottom - top) // 2

            if target < matrix[mid][0]:
                bottom = mid - 1

            elif target > matrix[mid][-1]:
                top = mid + 1

            else:
                break


        row = mid

        left, right = 0, COLS - 1

        while left <= right:
            mid = left + (right - left) // 2

            if target < matrix[row][mid]:
                right = mid - 1

            elif target > matrix[row][mid]:
                left = mid + 1

            else:
                return True

        return False
        