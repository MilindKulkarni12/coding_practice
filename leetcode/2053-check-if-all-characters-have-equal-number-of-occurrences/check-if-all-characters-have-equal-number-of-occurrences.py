class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = Counter(s)
        init = freq[s[0]]
        for i in range(1, len(s)):
            if freq[s[i]] != init:
                return False
        return True
