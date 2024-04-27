class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = {}
        
        def fx(r, k):
            if k == len(key):
                return 0
            if (r, k) in dp:
                return dp[(r, k)]
            res = float("inf")
            for i, c in enumerate(ring):
                if c == key[k]: # found
                    min_dist = min(abs(r - i), len(ring) - abs(r - i))
                    res = min(res, min_dist + 1 + fx(i, k + 1))
            dp[(r, k)] = res
            return res
        return fx(0, 0)

