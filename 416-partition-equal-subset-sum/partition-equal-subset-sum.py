class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        dp = [[-1]*(total//2 + 1) for _ in range(len(nums)+1)]

        def fx(i, rem):
            if rem == 0:
                return True
            if i == 0:
                return False
            if dp[i][rem] != -1:
                return dp[i][rem]
            if nums[i] <= rem:
                dp[i][rem] = fx(i-1, rem - nums[i]) or fx(i-1, rem)
            else:
                dp[i][rem] = fx(i-1, rem)
            return dp[i][rem]

        return fx(len(nums)-1, total//2) 
