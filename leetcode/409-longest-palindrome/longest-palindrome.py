class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        ans = 0
        odd = False
        for v in freq.values():
            if v % 2 == 0:
                ans += v
            else:
                ans += v - 1
                odd = True
        return ans + 1 if odd else ans
