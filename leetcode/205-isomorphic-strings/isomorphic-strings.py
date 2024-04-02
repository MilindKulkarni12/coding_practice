class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        f1 = Counter(s).keys()
        f2 = Counter(t).keys()
        if len(f1) != len(f2):
            return False
        for i in range(len(s)):
            val = d.get(s[i], -1)
            if val == -1:
                d[s[i]] = t[i]
            elif val != t[i]:
                return False
        return True
