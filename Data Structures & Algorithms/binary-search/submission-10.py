class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L, H = 0, len(nums) - 1

       

        while L <= H:
            mid = L + (H-L) // 2

            if target > nums[mid]:
                L = mid + 1

            elif target < nums[mid]:
                H = mid - 1

            else:
                return mid

        return -1


        