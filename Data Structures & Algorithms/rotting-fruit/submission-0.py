class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        #add all initial rotten fruits to the q
        # then count how many fresh fruits in total 
        #then run multisource bfs and process level by level
        #then at the end check if there are any fresh fruits that werent reached if not return count\

        ROWS, COLS = len(grid), len(grid[0])
        minute = 0
        fresh_fruits = 0
        q = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_fruits += 1
                elif grid[r][c] == 2:
                    q.append((r,c))


        while q and fresh_fruits > 0:
            
            level_size = len(q)
            for i in range(level_size):
                r,c = q.popleft()


                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh_fruits -= 1
            minute += 1

        if fresh_fruits != 0:
            return -1
        else:
            return minute


        