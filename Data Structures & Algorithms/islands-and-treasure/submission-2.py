class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #write the distance of each land cell from the nearest treasure chest
        #need to do a multi source bfs for an optimal solution 
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        INF = (2 ** 31) - 1
        q = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))


        while q:
            r,c = q.popleft()

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] not in visited and grid[nr][nc] == INF:
                    grid[nr][nc] = 1 + grid[r][c]
                    q.append((nr,nc))
                    visited.add((nr,nc))



        
        