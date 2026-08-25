class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0

        L, R = 0, len(heights) - 1


        while L <= R:
            area = min(heights[L], heights[R]) * (R-L)
            maxArea = max(maxArea, area)

            if heights[L] <= heights[R]:
                L += 1

            else:
                R -= 1

        return maxArea
        