class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        if n == 0:
            return True

        new_intervals = sorted(intervals, key=lambda x: x[0])
        
        s0, e0 = new_intervals[0]
        for i in range(1, n):
            s, e = new_intervals[i]
            if e0 > s:
                return False
            s0 = s
            e0 = e
        return True
