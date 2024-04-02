class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros_seen = ones_seen = 0
        count = Counter(s)
        ans = 0
        for c in s:
            if c == '0':
                ans += ones_seen * (count['1'] - ones_seen)
                zeros_seen += 1
            else:
                ans += zeros_seen * (count['0'] - zeros_seen)
                ones_seen += 1
        return ans
