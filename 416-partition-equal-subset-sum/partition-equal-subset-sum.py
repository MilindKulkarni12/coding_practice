class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            # odd
            return False

        # memoize
        dp = [ [False]*(total//2 + 1) for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            dp[i][0] = True
        # print(dp)
        for i in range(1, len(nums) + 1):
            for t in range(1, total//2 + 1):
                if nums[i - 1] <= t:
                    dp[i][t] = dp[i - 1][t - nums[i - 1]] or dp[i - 1][t]
                else:
                    dp[i][t] = dp[i - 1][t]
        return dp[len(nums)][total//2]
        
