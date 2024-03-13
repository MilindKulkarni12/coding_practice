class Solution:
    def pivotInteger(self, n: int) -> int:
        for x in range(n+1):
            xsum = (x*(x+1))//2
            nsum = (((2*x) + (n - x + 1 - 1))*(n - x + 1))//2 
            if xsum == nsum:
                return x
        return -1
