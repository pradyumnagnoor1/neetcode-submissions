class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1 #gives be the indexes of the rows

        while top <= bottom: #binary search algorithm
            mid = top + (bottom - top) // 2 # mid row basically

            if target < matrix[mid][0]: # checking if target is less than smallest value in row
                bottom = mid - 1 

            elif target > matrix[mid][-1]: # checking if target is grater than biggest value in row
                top = mid + 1

            else: # right row has been found 
                break

        if not (top <= bottom): # if binary search fails return False
                return False

        row = (top + bottom) // 2 # store the right row index in this variable

        l, r = 0, COLS - 1 # pointers for binary search in the row

        while l <= r: # regular binary search
            mid = l + (r-l) // 2
            if target < matrix[row][mid]: # does check in the row we stored in the variable before
                r = mid - 1

            elif target > matrix[row][mid]: 
                l = mid + 1

            else:
                return True

        return False 

        

        