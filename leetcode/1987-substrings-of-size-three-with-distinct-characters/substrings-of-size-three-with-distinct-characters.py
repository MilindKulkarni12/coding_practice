class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 2):
            d = {}
            good = True
            for j in s[i: i + 3]:
                if d.get(j, -1) == -1:
                    d[j] = True
                else:
                    good = False
                    break
            if good:
                ans += 1
        return ans