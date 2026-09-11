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
        





        # max_profit = 0

        # for i, x in enumerate(prices):

        #     for j, y in enumerate(prices):

        #         if i < j and max_profit < y - x:
        #             max_profit = y - x
        
        # return max_profit

