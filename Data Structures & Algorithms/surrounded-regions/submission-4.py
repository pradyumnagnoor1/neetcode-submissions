class Solution:
    def solve(self, board: List[List[str]]) -> None:
        "turn every O into a X if its not on the edge"
        "can do this by first adding all edge nodes to set"
        "and then running a dfs on a cell if its a O"
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visited or board[r][c] != 'O':
                return 

            visited.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for c in range(COLS): 
            dfs(0,c) #im starting at row 0 and visiting each cell in left col
            dfs(ROWS - 1, c) #starting at rightmost row denotd by ROWS - 1

        for r in range(ROWS): #need to revise the bounds 
            dfs(r, 0) # 0 denotes starting at the first col which is top row
            dfs(r, COLS - 1) #cols - 1 denotes starting at the bottom row

        for r in range(ROWS):
            for c in range(COLS):
                if 0 <= r < ROWS and 0 <= c < COLS and (r,c) not in visited and board[r][c] == 'O':
                    board[r][c] = 'X'

        


        