class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        n, m = len(s), len(t)
        ans = m
        while i < n and j < m:
            if s[i] == t[j]:
                ans -= 1
                j += 1
            i += 1
        return ans
       