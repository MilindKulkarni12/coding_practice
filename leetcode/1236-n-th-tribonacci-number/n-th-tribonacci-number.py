class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = t2 = 1
        if n == 0:
            return t0
        elif n == 1:
            return t1
        elif n == 2:
            return t2

        i = 2
        t = 0
        while i < n:
            t = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = t
            i += 1
        return t
 