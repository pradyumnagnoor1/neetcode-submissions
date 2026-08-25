class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []


        def backtracking(start, total, path):
            if total == target:
                res.append(path.copy())
                return

            if total > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i, total + nums[i], path)
                path.pop()

        backtracking(0, 0, [])

        return res

        