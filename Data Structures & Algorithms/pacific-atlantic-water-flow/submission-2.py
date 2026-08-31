class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()
        res = []

        def dfs(r, c, visited, prevHeight): #uses generic set 
            if ((r,c) in visited or r < 0 or c < 0 or r == ROWS or c == COLS or prevHeight > heights[r][c]): #going from bottom up so we are cehcking if the previous is lower than next height
                return 

            visited.add((r,c)) #added if cell not in set, in bounds, and is greater than prev height
            dfs(r+1, c, visited, heights[r][c]) #adds current cell as prev height for next dfs call
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r , c-1, visited, heights[r][c])


        for c in range(COLS): #top and bottom 
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS): #left and right
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])


        for r in range(ROWS): #brute force cehck to see if any cells are in both sets
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res #list of lists coordinates in both sets 

        