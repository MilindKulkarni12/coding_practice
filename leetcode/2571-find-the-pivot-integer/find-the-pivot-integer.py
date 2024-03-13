class Solution:
    def pivotInteger(self, n: int) -> int:
        nsum = (n*(n+1))//2
        for x in range(n+1):
            xsum = (((2*x) + (n - x + 1 - 1))*(n - x + 1))//2 
            if xsum == (nsum - xsum + x):
                return x
        return -1
