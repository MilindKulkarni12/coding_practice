class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0
        """
            1101101
            1 swap = 1
            1 swap = 2
            0 0111101
            1 swap = 3
            1 swap = 4
            0 0011111
            1 swap = 5

        """
        l, r = 0, n - 1
        swaps = total = 0
        while l < n:
            if s[l] == '0':
                l += 1
                total += swaps
            else:
                swaps += 1
                l += 1
        return total


