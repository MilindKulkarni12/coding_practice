class Solution:
    def minimumKeypresses(self, s: str) -> int:
        freq = Counter(s)
        freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        i = clicks = 0
        offset = 1
        for k in freq.keys():
            clicks += freq[k]*offset
            i += 1
            if i == 9:
                offset += 1
                i = 0
        return clicks