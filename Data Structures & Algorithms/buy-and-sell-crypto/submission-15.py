class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        L = 0 
        profit = 0


        for R in range(1, len(prices)): #start at second number 
            if prices[R] < prices[L]: # if the right number is greater than change the left pointer
                L = R

            else:
                profit = max(profit, prices[R] - prices[L]) #finds max profit


        return profit 
        