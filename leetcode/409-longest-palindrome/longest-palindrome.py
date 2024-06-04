class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        if len(freq) == 1:
            return len(s)
        # print(freq)
        ans = 0
        odd = []
        for v in freq.values():
            if v % 2 == 0:
                ans += v
            else:
                odd.append(v)
        odd.sort(reverse=True)
        if odd:
            ans += odd[0]
            for o in odd[1:]:
                ans += o - 1
        return ans
