class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left, right = 0, 1
        n = len(prices)
        if n == 1:
            return 0
        
        while right != n:
            if prices[left] > prices[right]:
                left = right
            else:
                profit = max(profit, prices[right] - prices[left])
            right += 1
        return profit