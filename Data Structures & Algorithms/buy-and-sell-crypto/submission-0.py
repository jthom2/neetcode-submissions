class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        max_profit = 0

        for i, x in enumerate(prices):

            for j, y in enumerate(prices):

                if i < j and max_profit < y - x:
                    max_profit = y - x
        
        return max_profit

