class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = {}

        def fx(i, r1, r2):
            if r1 < 0 or r1 >= m or r2 < 0 or r2 >= m:
                return -inf
            key = f'{i}|{r1}|{r2}'
            if dp.get(key, -1) != -1:
                return dp.get(key)

            res = grid[i][r1]
            if r1 != r2:
                res += grid[i][r2]
            if i == n-1:
                dp[key] = res
                return res
            res += max(fx(i+1, new_col1, new_col2)
                              for new_col1 in [r1, r1+1, r1-1]
                              for new_col2 in [r2, r2+1, r2-1])
            dp[key] = res
            return res
        
        return fx(0, 0, len(grid[0])-1)
