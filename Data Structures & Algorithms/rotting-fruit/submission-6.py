class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        fresh_fruits = 0
        minutes = 0


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_fruits += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
                

        
        while q and fresh_fruits > 0:
            size = len(q)
            for i in range(size):
                r,c = q.popleft()

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:

                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh_fruits -= 1

            minutes += 1

        if fresh_fruits == 0:
            return minutes
        else:
            return -1




        