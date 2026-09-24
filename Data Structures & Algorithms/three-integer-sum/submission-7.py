class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = set()

        for i, num in enumerate(nums):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    if (nums[i], nums[j], nums[k]) not in visited:
                        visited.add((nums[i], nums[j], nums[k]))
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1

        return res