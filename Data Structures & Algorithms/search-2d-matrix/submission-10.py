class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        "run binary search twice to achieve desired run time"
        "Run binary search on rows first to find right row"
        "Then once the right row has been found run regular binary search on the right row"


        ROWS, COLS = len(matrix), len(matrix[0])


        top, bottom = 0, ROWS - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target > matrix[mid][-1]:
                top = mid + 1

            elif target < matrix[mid][0]:
                bottom = mid - 1

            else:
                break

        right_row = mid  

        left, right = 0, COLS - 1

        while left <= right:
            mid = (left + right) // 2

            if target > matrix[right_row][mid]:
                left = mid + 1

            elif target < matrix[right_row][mid]:
                right = mid - 1

            else:
                return True

        return False      