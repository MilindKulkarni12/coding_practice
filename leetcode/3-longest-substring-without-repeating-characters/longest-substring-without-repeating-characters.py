class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        
        l = r = 0
        sbs = set()
        max_len = 0
        while r != n:
            if l == r:
                sbs.add(s[r])
                r += 1
                max_len = max(max_len, len(sbs))
            elif s[r] not in sbs:
                sbs.add(s[r])
                r += 1
                max_len = max(max_len, len(sbs))
            else:
                sbs.remove(s[l])
                l += 1
        return max_len
