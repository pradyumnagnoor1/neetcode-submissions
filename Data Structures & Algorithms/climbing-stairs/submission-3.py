class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}

        def dfs(i):

            if i == n: #base case that means i reached the top so recursive call returns 1
                return 1

            if i > n: #overshot the top number so its not a valid path
                return 0

            if i in cache: #checks if i have solved this before
                return cache[i] #if yes then reuse the saved answer

            cache[i] = dfs(i + 1) + dfs(i + 2)

            return cache[i]

        return dfs(0)


        