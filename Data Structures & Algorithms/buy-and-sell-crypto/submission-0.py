class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1

        maxProfit = 0

        length = len(prices)
        while (j < length):
            profit = prices[j] - prices[i]
            maxProfit = max(maxProfit, profit)
            if profit < 0:
                i = j
            j += 1
        return maxProfit