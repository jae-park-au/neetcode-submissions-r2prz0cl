class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        buy, sell = 0, 1
        cur_max = 0
        while sell < len(prices):
            diff = prices[sell] - prices[buy]

            if diff <= 0:
                buy = sell
                sell += 1
            else:
                cur_max = max(cur_max, diff)
                sell += 1


        return cur_max