class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        freq_sorted = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        op = ''
        for k in freq_sorted:
            op += f'{k}'*freq[k]
        return op
