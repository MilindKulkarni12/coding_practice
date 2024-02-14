class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        def fx(s, l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        for i in range(len(s)):
            count += fx(s, i, i)
            count += fx(s, i, i+1)

        return count
