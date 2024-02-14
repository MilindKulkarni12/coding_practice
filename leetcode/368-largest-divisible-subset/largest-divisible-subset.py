class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        dp = [1] * len(nums)
        max_len = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums_sorted[i] % nums_sorted[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max_len = max(max_len, dp[i])
        
        ans = []
        prev = -1
        for i in range(len(nums)-1, -1, -1):
            if dp[i] == max_len and (prev == -1 or (prev % nums_sorted[i] == 0)):
                ans.append(nums_sorted[i])
                max_len -= 1
                prev = nums_sorted[i]
        
        return ans
