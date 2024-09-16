class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = []
        for tp in timePoints:
            h, m = map(int, tp.split(':'))
            t = h * 60 + m
            time.append(t)
        
        time.sort()
        min_diff = 1500
        for i in range(1, len(time), 1):
            min_diff = min(min_diff, time[i] - time[i-1])
        return min(min_diff, 24*60 - time[-1] + time[0])
