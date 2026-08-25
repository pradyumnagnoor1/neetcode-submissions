class Solution:
    def rob(self, nums: List[int]) -> int:

        cache1 = {}
        cache2 = {}

        if len(nums) == 1:
            return nums[0]

        def dfs1(i):
             
            if i >= len(nums) - 1:
                return 0

            if i in cache1:
                return cache1[i]

            rob = nums[i] + dfs1(i + 2)
            skip = dfs1(i + 1)

            cache1[i] = max(rob, skip)

            return cache1[i]

        def dfs2(i):

            if i >= len(nums):
                return 0

            if i in cache2:
                return cache2[i]

            rob = nums[i] + dfs2(i + 2)
            skip = dfs2(i+1)

            cache2[i] = max(rob, skip)

            return cache2[i]

        return max(dfs1(0), dfs2(1))




            

        