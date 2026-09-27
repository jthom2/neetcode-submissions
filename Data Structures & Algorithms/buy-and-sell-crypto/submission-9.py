class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(len(prices)-1,-1,-1):
            try: p = prices[i] - min(prices[:i])
            except: p = 0
            profit = max(profit, p)
        
        return profit