class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = {word: Counter(word) for word in words}
        ans = []
        for i in range(97, 124):
            min_occ = 101
            zero_occ = False
            for d in freq:
                if freq[d][chr(i)] == 0:
                    zero_occ = True    
                    break
                else:
                    min_occ = min(min_occ, freq[d][chr(i)])
            if not zero_occ:
                ans.extend([chr(i)]*min_occ)
        return ans
