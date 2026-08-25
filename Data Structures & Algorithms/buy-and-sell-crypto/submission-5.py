class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0
        L = 0


        for R in range(len(prices)):
            if prices[L] > prices[R]:
                L = R

            else:
                profit_max = max(profit_max, prices[R] - prices[L])


        return profit_max
                
        