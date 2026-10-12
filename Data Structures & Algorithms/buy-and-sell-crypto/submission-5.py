class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        r = 1
        
        max_profit = 0
        out = 0
        
        while l<r and r<n:
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)

            if prices[r] >= prices[l]:
                r += 1

            if r < n and prices[r] < prices[l]:
                l = r
                r = r+1
            
            if r >= n:
                break

            
        return max_profit