class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n < 3:
            return t[n]

        i = 2
        curr = 0
        while i < n:
            # print(i, t)
            curr = t[2] + t[1] + t[0]
            t[0] = t[1]
            t[1] = t[2]
            t[2] = curr
            i += 1
        return t[2]
 