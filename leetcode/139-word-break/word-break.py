class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # def fx(curr_str, i):
        #     if len(curr_str) == curr_str.count('*'):    
        #         return True
        #     if i >= len(wordDict):
        #         return False
        #     if wordDict[i] in curr_str:
        #         curr_str1 = curr_str.replace(wordDict[i], '*', 1)
        #         return fx(curr_str1, i) or fx(curr_str, i+1)
        #     else:
        #         return fx(curr_str, i+1)
        # return fx(s, 0)
        n = len(s)
        words = set(wordDict)
        dp = [False]*(n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j: i] in words:
                    dp[i] = True
                    break
        return dp[-1]

