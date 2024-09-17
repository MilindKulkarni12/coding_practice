class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        w1 = s1.split()
        w2 = s2.split()
        f = {}
        for w in w1:
            if w in f:
                c, p = f[w]
                f[w] = [c+1, p]
            else:
                f[w] = [1, False]
        for w in w2:
            # f[w] += 1 if f[w] <= 0 else -1
            if w in f and f[w][0] > 0:
                f[w][0] -= 1
                f[w][1] = True
            else:
                if w in f:
                    f[w][0] += 1
                else:
                    f[w] = [1, False]
        return [k for k, v in f.items() if v[0] == 1 and v[1] is False]
