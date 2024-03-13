class Solution:
    def pivotInteger(self, n: int) -> int:
        nsum = (n*(n+1))//2
        isum = prev = 0
        for x in range(n+1):
            isum += x
            xsum = nsum - prev
            prev = isum
            if xsum == isum:
                return x
        return -1
