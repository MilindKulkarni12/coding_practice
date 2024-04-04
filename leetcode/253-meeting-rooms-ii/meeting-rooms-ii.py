class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        new_intervals = sorted(intervals, key=lambda x: x[0])
        rooms = []

        heapq.heappush(rooms, new_intervals[0][1])
        for i in new_intervals[1:]:
            if rooms[0] <= i[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i[1])
        return len(rooms)

        return rooms