class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        lowest_price = prices[0]

        for n in prices:
            lowest_price = min(lowest_price, n)
            profit = n - lowest_price
            max_profit = max(profit, max_profit)

                    


        print(max_profit)

        return max_profit
        


