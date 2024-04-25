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

        # def fx(subseq, i):
        #     if i == n:
        #         # print(s1)
        #         return 0
            
        #     if (subseq, i) in dp:
        #         return dp[(subseq, i)]
        #     if (not subseq) or  (abs(ord(s[i]) - ord(subseq[-1])) <= k):
        #         dp[(subseq, i)] = 1 + max(fx(subseq, i + 1), fx(subseq + s[i], i + 1))
        #     else:
        #         dp[(subseq, i)] = 1 + fx(subseq, i + 1) 
        #     return dp[(subseq, i)]
        # return fx('', 0)
