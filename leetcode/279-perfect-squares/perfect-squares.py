class Solution:
    def numSquares(self, n: int) -> int:
        max_square_root = int(sqrt(n))
        dp = [0] + [n] * n
      
        for i in range(1, max_square_root + 1):
            square = i * i
            for j in range(square, n + 1):
                dp[j] = min(dp[j], dp[j - square] + 1)
      
        return dp[n]
