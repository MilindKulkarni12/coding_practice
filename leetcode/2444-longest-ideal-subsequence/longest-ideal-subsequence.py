class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26

        for c in s:
            curr = ord(c) - ord('a')
            longest = 0
            for prev in range(26):
                if abs(curr - prev) <= k:
                    longest = max(longest, 1 + dp[prev])
            dp[curr] = max(longest, dp[curr])
        return max(dp)

        # n = len(s)
        # self.max_len = -1
        # dp = {}

        # def fx(prev, i):
        #     if i == n:
        #         # print(s1)
        #         return 0
        #     if (prev, i) in dp:
        #         return dp[(prev, i)]
        #     if (not prev) or  (abs(ord(s[i]) - ord(prev)) <= k):
        #         dp[(prev, i)] = max(1 + fx(s[i], i + 1), fx(prev, i + 1))
        #     else:
        #         dp[(prev, i)] = fx(prev, i + 1) 
        #     return dp[(prev, i)]
        # return fx('', 0)
