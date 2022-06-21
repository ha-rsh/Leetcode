from sys import maxsize

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = -maxsize
        profit = 0
        curr_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > curr_min:
                profit = max(prices[i] - curr_min, profit)
                
            
            curr_min = min(prices[i], curr_min)
            
        return profit
        