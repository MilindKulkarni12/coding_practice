class Solution:
    def makeGood(self, s: str) -> str:

        flag = False
        while not flag:
            new_s = ''
            i = 0
            flag = True
            n = len(s)
            while i < n:
                # print(s, new_s, i)
                if i < n-1 and ((s[i].isupper() and (s[i].lower() == s[i+1]))
                    or (s[i+1].isupper() and (s[i+1].lower() == s[i]))):
                    i += 2
                    flag = False
                else:
                    new_s += s[i]
                    i += 1
            s = new_s
        return s
