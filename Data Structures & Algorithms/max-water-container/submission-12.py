class Solution:
    def maxArea(self, heights: List[int]) -> int:

        L = 0
        R = len(heights) - 1
        maxArea = 0


        while L < R:
            area = min(heights[L], heights[R]) * (R-L)
            maxArea = max(area, maxArea)


            if heights[L] < heights[R]:
                L += 1

            elif heights[L] > heights[R]:
                R -= 1

            else:
                L += 1 # dont break increment either L or R since they are the same height

        return maxArea
