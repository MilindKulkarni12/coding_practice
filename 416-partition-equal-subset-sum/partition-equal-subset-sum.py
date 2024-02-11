class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            # odd
            return False

        # memoize
        dp = [ [-1]*(total//2 + 1) for _ in range(len(nums) + 1)]

        def fx(n, total):
            if total == 0:
                # reqd sum achieved
                return True
            if n == 0:
                # list parsed compeletely
                return False
            
            # check if already parsed
            if dp[n-1][total] != -1:
                return dp[n-1][total]

            if nums[n - 1] <= total:
                # include OR exclude
                dp[n-1][total] = fx(n - 1, total - nums[n - 1]) or fx(n - 1, total)
            # move to next
            else:
                dp[n-1][total] = fx(n - 1, total)
            
            return dp[n-1][total]

        return fx(len(nums), total //2)
