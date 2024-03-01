class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        freq = Counter(s)
        f1, f0 = freq.get('1', 0), freq.get('0', 0)
        ans = ''
        for i in range(f1 - 1):
            ans += '1'
            freq['1'] -= 1

        for i in range(f0):
            ans += '0'
        
        if freq['1'] > 0:
            ans += '1'
        return ans 
        