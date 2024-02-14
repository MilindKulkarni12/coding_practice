class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # s1 = positives, s2 = negatives
        # s1 + s2 = s
        # s1 - s2 = t
        # 2s1 = s + t
        # s1 = (s + t) // 2
        if target < 0:
            target = abs(target)
            
        sum_nums = sum(nums)
        n_tar = sum_nums + target
         
        if sum_nums < target:
            return 0
        if n_tar % 2 != 0:
            return 0
        
        n_tar = n_tar // 2
        dp = [[0]*(n_tar + 1) for _ in range(len(nums) + 1)]
        for i in range(len(nums)+1):
            dp[i][0] = 1
        # dp[0][0] = 1
        for i in range(1, len(nums) + 1):
            for j in range(n_tar + 1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j - nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        # for i in dp:
        #     print(dp)
        return dp[len(nums)][n_tar]
