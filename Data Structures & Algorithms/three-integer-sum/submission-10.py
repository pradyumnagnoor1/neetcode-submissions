class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = set()
        res = []

        for i, value in enumerate(nums):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    if (nums[i], nums[j], nums[k]) not in visited:
                        visited.add((nums[i], nums[j], nums[k]))
                        res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                   
        return res