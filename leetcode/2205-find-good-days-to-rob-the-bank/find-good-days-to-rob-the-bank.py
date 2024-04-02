class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # dec = [0, 1, 2, 3, 0, 0, 1]
        # inc = [0, 4, 3, 2, 1, 0, 0]
        n = len(security)
        inc, dec = [0]*n, [0]*n
        i, j = 0, n - 1
        while i < n:
            if i > 0 and security[i] <= security[i-1]:
                inc[i] = inc[i - 1] + 1
            if j < n-1 and security[j] <= security[j+1]:
                dec[j] = dec[j + 1] + 1
            i += 1
            j -= 1
        ans = []
        for i in range(time, n - time):
            if inc[i] >= time and dec[i] >= time:
                ans.append(i)
        return ans

